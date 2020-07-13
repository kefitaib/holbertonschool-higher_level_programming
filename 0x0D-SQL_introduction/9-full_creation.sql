-- task 9
-- creates a table called second_table in the current database.
CREATE TABLE IF NOT EXISTS second_table (id INT ,
       name VARCHAR(256), score INT);

-- Insert row 1
INSERT INTO second_table VALUES(1, "John", 10);

-- Insert row 2
INSERT INTO second_table VALUES(2, "Alex", 3);

-- Insert row 3
INSERT INTO second_table VALUES(3, "Bob", 14);

-- Insert row 4
INSERT INTO second_table VALUES(4 , "George", 8);
