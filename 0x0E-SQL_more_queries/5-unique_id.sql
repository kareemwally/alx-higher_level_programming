-- that script to create a unique id with default value
CREATE TABLE IF NOT EXISTS unique_id(
id INT UNIQUE DEFAULT 1,
name VARCHAR(256)
);
