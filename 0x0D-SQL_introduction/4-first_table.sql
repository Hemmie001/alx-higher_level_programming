-- this script creates a table called first_table in the current database 
-- ...in my MySQL server.
-- Such that, the database name will be passed as an argument of the 
-- ...mysql command if the first_table already exist, 
-- the script should not fail
CREATE TABLE IF NOT EXISTS first_table
(
    id INT,
    name VARCHAR(256)
);
