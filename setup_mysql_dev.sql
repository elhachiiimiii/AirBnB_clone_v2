-- Write a script that prepares a MySQL server for the project
-- should script not fail If database or user already exists

-- create hbnbb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- create new user if not exists
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- grant all privileges
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
