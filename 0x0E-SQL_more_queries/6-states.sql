-- creates a database hbtn_0d_usa
-- creates a table states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id int UNIQUE NOT NULL AUTO_INCREMENT, name varchar(256) NOT NULL, PRIMARY KEY (id));
