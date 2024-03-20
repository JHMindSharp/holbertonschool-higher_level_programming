# SQL - More Queries

## Description

This project is part of the curriculum of Holberton School. It aims to deepen the understanding of SQL, focusing on more advanced queries, user privileges management, and the relationship between tables within a database.

### Learning Objectives

- How to create a new MySQL user
- How to manage privileges for a user to a database or table
- Understanding of PRIMARY and FOREIGN keys
- Utilization of NOT NULL and UNIQUE constraints
- How to retrieve data from multiple tables in one request
- Usage of subqueries, JOIN and UNION

## Prerequisites

- MySQL 8.0 (Version 8.0.25 or later)
- Basic knowledge of SQL syntax and commands
- Understanding of relational database concepts

## Installation

To set up the project environment, follow these steps:

1. Update your system:
    ```bash
    sudo apt update
    ```

2. Install MySQL server on Ubuntu 20.04 LTS:
    ```bash
    sudo apt install mysql-server
    ```

3. Verify the installation by checking the MySQL version:
    ```bash
    mysql --version
    ```

4. Connect to your MySQL server:
    ```bash
    sudo mysql
    ```

## Usage

Each SQL script in this project performs a specific operation related to the project's learning objectives. To execute a script, use the following command:

```bash
mysql -u root -p <database_name> < script_name.sql
```
Replace <database_name> with the name of your database, and script_name.sql with the name of the SQL script you wish to execute.

## Contribution
Contributions to this project are welcome. To contribute:

1. Fork the project repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes with descriptive commit messages.
4. Push your branch to your fork.
5. Submit a pull request to the original repository.

## Authors

Guillaume Salva - Creator
Jonathan Huybrechts - Contributor

## Acknowledgments
Holberton School for providing the project guidelines and learning resources.