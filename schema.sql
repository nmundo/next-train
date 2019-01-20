CREATE TABLE IF NOT EXISTS stations (id INT PRIMARY KEY, name VARCHAR);
CREATE TABLE IF NOT EXISTS timeslots (id INT PRIMARY KEY, day VARCHAR, station INT, time TIME);

INSERT INTO stations (id, name)
VALUES
  (0, 'UNC Charlotte'),
  (1, 'JW Clay'),
  (2, 'McCullough'),
  (3, 'University City Boulevard'),
  (4, 'Tom Hunter'),
  (5, 'Old Concord Road'),
  (6, 'Sugar Creek'),
  (7, '36th St'),
  (8, '25th St'),
  (9, 'Parkwood'),
  (10, '9th St'),
  (11, '7th St'),
  (12, 'CTC/Arena'),
  (13, '3rd St'),
  (14, 'Stonewall'),
  (15, 'Carson'),
  (16, 'Bland St'),
  (17, 'East/West'),
  (18, 'New Bern'),
  (19, 'Scaleybark'),
  (20, 'Woodlawn'),
  (21, 'Tyvola'),
  (22, 'Archdale'),
  (23, 'Arrowood'),
  (24, 'Sharon Rd West'),
  (25, 'I-485');