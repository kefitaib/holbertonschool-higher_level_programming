-- task 5
-- create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- creates the table states
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states
(id INT PRIMARY KEY NOT NULL UNIQUE AUTO_INCREMENT,
       name VARCHAR(256));
