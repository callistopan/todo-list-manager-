
DROP TABLE IF EXISTS todo;



CREATE TABLE todo(
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       content TEXT,
       date_created DATE DEFAULT (datetime('now','localtime')),
       date_ended DATE,
       over_due TEXT,
       completed integer

);


