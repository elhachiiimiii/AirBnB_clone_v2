-- Write a script that prepares a MySQL server for the project
-- should script not fail If database or user already exists

-- create new hbnb_test_db is not exists
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- create hbnbb_dev_db
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- grant all privileges
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
