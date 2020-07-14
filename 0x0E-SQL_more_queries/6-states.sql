-- task 5
-- create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- creates the table hbtn_0d_usa on your MySQL server
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states
(id INT NOT NULL DEFAULT 1 UNIQUE PRIMARY KEY,
       name VARCHAR(256));
