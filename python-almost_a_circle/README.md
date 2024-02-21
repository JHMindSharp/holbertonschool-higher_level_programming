# Python Almost a Circle

## Description
Python Almost a Circle is a project focused on reviewing various Python concepts such as classes, inheritance, serialization, unit testing, and file handling. The project consists of implementing classes for managing geometric shapes like rectangles and squares.

## Project Structure
The project consists of the following files and directories:

- **models/**: Directory containing Python files for different classes.
  - **base.py**: Defines the `Base` class.
  - **rectangle.py**: Defines the `Rectangle` class.
  - **square.py**: Defines the `Square` class.
- **tests/**: Directory containing unit test files for the classes.
- **README.md**: This file provides an overview of the project.
- **.gitignore**: Specifies intentionally untracked files to ignore.
- **AUTHORS**: Contains the names of contributors to the project.

## Class Descriptions
1. **Base**: The base class that manages the ID attribute for other classes. Includes methods for serialization and deserialization.
2. **Rectangle**: Represents a rectangle shape. Inherits from the `Base` class. Includes methods for calculating area, displaying the shape, updating attributes, and converting to a dictionary.
3. **Square**: Represents a square shape, which is a special case of a rectangle. Inherits from the `Rectangle` class. Includes methods for updating attributes and converting to a dictionary.

## Requirements
- Python 3.8.5 or higher
- Pycodestyle for code style enforcement
- Unittest module for running unit tests

## Usage
To use the classes defined in this project, import them into your Python scripts as follows:

python
from models.rectangle import Rectangle
from models.square import Square
Then, you can create instances of Rectangle and Square and perform various operations on them.

## Testing
``python3 -m unittest discover``

This will run all the unit tests defined in the test files.

## AUTHORS
Miniknacky
