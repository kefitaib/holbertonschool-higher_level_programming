-- task 1
-- creates the MySQL server user user_0d_1
CREATE USER user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';

-- grant privileges
GRANT ALL ON *.* TO user_0d_1@localhost;

-- apply
FLUSH PRIVILEGES;
