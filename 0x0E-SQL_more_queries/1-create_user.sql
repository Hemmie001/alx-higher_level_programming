-- This script creates the MySQL server user user_0d_1. and:
-- *gives all privileges on your MySQL server to the user.
-- *set user_0d_1_pwd as password to the user
-- *and not fail if the user already exist.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
SET PASSWORD FOR 'user_0d_1'@'localhost' = PASSWORD('user_0d_1_pwd');
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
FLUSH PRIVIiLEGES;
