-- Create states table in hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db .* TO 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT SELECT ON performance_schema .* TO 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT USAGE ON *.* TO 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
FLUSH PRIVILEGES;
