CREATE TABLE IF NOT EXISTS stations (id INTEGER PRIMARY KEY, name TEXT, lat REAL, lon REAL, address TEXT, zip INTEGER);
CREATE TABLE IF NOT EXISTS timeslots (id INT PRIMARY KEY, day VARCHAR, station INT, time TIME);
