-- task 7
-- create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- creates the table cities
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities
(id INT PRIMARY KEY NOT NULL UNIQUE AUTO_INCREMENT,
    state_id INT NOT NULL, name VARCHAR(256) NOT NULL,
    FOREIGN KEY(state_id) REFERENCES states(id));
