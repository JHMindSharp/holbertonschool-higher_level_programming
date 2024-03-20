-- Creates the table unique_id with id INT default 1, must be unique, and name VARCHAR(256).
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256),
    PRIMARY KEY (id)
);
