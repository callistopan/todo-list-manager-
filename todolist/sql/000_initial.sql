DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS tags_pets;
DROP TABLE IF EXISTS animal;
DROP TABLE IF EXISTS tag;
DROP TABLE IF EXISTS pet;
DROP TABLE IF EXISTS todo;



CREATE TABLE todo(
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       content TEXT NOT NULL,
       date_created DATE DEFAULT (datetime('now','localtime'))

);


