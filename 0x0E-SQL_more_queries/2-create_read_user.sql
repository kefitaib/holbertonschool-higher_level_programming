-- task 2
-- creates the database hbtn_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0c_2;

-- create user user_0d_2
CREATE USER user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';

-- grant privileges
GRANT USAGE ON *.* TO user_0d_2@localhost;

-- 2
GRANT SELECT ON hbtn_0c_2.* TO user_0d_2@localhost;

-- apply
FLUSH PRIVILEGES;
