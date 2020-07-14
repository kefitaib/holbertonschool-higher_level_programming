-- task 5
-- create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- creates the table states
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states
(id INT PRIMARY KEY NOT NULL DEFAULT 1 AUTO_INCREMENT UNIQUE,
       name VARCHAR(256));
