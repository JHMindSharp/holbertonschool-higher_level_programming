-- Creates the table force_name with id and name columns, name can't be null.
CREATE TABLE IF NOT EXISTS force_name (
    id INT AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
