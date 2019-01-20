from flask import Flask, jsonify, render_template, g
from datetime import datetime
import json
import sqlite3

app = Flask(__name__)

DATABASE = './database.db'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print('Initialized the database.')


@app.route('/next_train/')
def station_list():
    db = get_db()
    cur = db.execute('SELECT id, name FROM stations ORDER BY id DESC')
    stations = cur.fetchall()
    cur.close()
    return render_template('station_list.html', stations=stations)


@app.route('/next_train/<string:station_id>')
def see_next_train(station_id):
    next_train = get_next_train(station_id)
    db = get_db()
    cur = db.execute(f'SELECT name FROM stations WHERE id = {station_id}')
    station = cur.fetchone()[0]
    cur.close()
    return render_template('next_train.html', station=station, next_train=next_train)


# TODO: Why is this a string and not an int..?
@app.route('/api/<string:station_id>/')
@app.route('/api/<string:station_id>/<string:direction>/')
def get_next_train_json(station_id, direction=None):
    next_train = get_next_train(station_id, direction)
    return jsonify(next_train)


def get_next_train(station_id, direction=None):

    current_time = datetime.strptime(str(datetime.now().time()), '%H:%M:%S.%f')

    timetables = {
        'inbound': [],
        'outbound': []
    }

    next_train = {
        'inbound': None,
        'outbound': None
    }

    current_day = datetime.today().weekday()
    if current_day <= 4:
        day = 'weekday'
    elif current_day == 5:
        day = 'saturday'
    else:
        day = 'sunday'

    if direction is None or direction == 'inbound':
        with open(f'{day}/inbound.json', 'r') as f:
            timetables['inbound'] = json.load(f)

        for timepoint in timetables['inbound'][station_id]:
            if timepoint != '-----':
                if datetime.strptime(timepoint, '%I:%M %p') < current_time:
                    pass
                else:
                    next_train['inbound'] = timepoint
                    break

    if direction is None or direction == 'outbound':
        with open(f'{day}/outbound.json', 'r') as f:
            timetables['outbound'] = json.load(f)

        for timepoint in timetables['outbound'][station_id]:
            if timepoint != '-----':
                if datetime.strptime(timepoint, '%I:%M %p') < current_time:
                    pass
                else:
                    next_train['outbound'] = timepoint
                    break

    return next_train


if __name__ == '__main__':
    app.run()
