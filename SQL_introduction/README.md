![SQL](https://image.noelshack.com/fichiers/2024/12/1/1710757692-miniknacky-une-photo-deinstein-inventant-le-sql-sur-un-tableau-2b0f27fe-1417-4bac-882a-5851f63bcd07.jpg)
# SQL - Introduction

## Overview

This project aims to introduce the fundamentals of SQL, focusing on the basics of databases, SQL syntax, and common operations within the MySQL database management system. Participants will gain hands-on experience with creating, modifying, and querying databases using SQL.

## Author

- Guillaume

## Level

- Novice

## Weight

- 1

## Learning Objectives

By the end of this project, participants should be able to:

- Understand what databases are and their importance.
- Differentiate between relational databases and other types of databases.
- Explain the purpose and functionality of SQL.
- Describe the role and features of MySQL.
- Perform basic database operations such as creating and deleting databases in MySQL.
- Understand the difference between Data Definition Language (DDL) and Data Manipulation Language (DML).
- Create, alter, and query tables using SQL.
- Insert, update, and delete data within tables.
- Utilize subqueries in SQL operations.
- Apply MySQL functions in data manipulation and queries.

## Requirements

- **Editors**: vi, vim, emacs.
- **Environment**: All scripts will be tested on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25).
- **Conventions**:
  - Files must end with a newline.
  - SQL queries must include a comment before the query.
  - The first line in all files should be a comment describing the task.
  - All SQL keywords must be in uppercase (e.g., `SELECT`, `WHERE`).

## Setup

To prepare for this project, ensure MySQL 8.0 is installed and running on Ubuntu 20.04 LTS. Follow these steps to install MySQL and verify its version:

\```bash
sudo apt update
sudo apt install mysql-server
mysql --version
\```

## Usage

To execute the SQL scripts, use the following command syntax, replacing `<script.sql>` with your SQL script file:

\```bash
cat <script.sql> | mysql -hlocalhost -uroot -p
\```

## Resources

Participants are encouraged to review the following resources:

- What is Database & SQL?
- Install MySQL (MySQL Server)
- A Basic MySQL Tutorial
- Basic SQL statements: DDL and DML
- Basic queries: SQL and RA
- SQL technique: functions
- SQL technique: subqueries
- MySQL Cheat Sheet
- MySQL 8.0 SQL Statement Syntax

## Contributions

This project is part of the Holberton School Higher Level Programming curriculum. Contributions, suggestions, and feedback are welcome.

## License

This project is licensed under the terms of the Holberton School.
