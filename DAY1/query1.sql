create DATABASE Challenge; 
-- Creating a database

USE Challenge;
-- initializing the database

CREATE TABLE movies(
Id int,
Title varchar(225),
Year int);
-- Creating a table for movies

INSERT INTO movies(Id,Title,Year) values
(1,'Kung fu Panda',1997),
(2,'Home alone',1990),
(3,'Star Wars',1977),
(4,'Jurassic Park',1979),
(5,'Iron man',1989);
-- inserting values into the table