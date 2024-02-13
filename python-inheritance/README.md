# Python - Inheritance

## Description

This project is an exploration of inheritance in Python. It covers the creation and implementation of superclasses (parent classes) and subclasses, usage of inherited methods and attributes, and the implementation of multiple inheritance. The project aims to solidify understanding of how Python's inheritance model works and how to effectively use it in program design.

## Learning Objectives

Upon completion of this project, learners are expected to understand:

- What a superclass, baseclass, or parent class is
- What a subclass is
- How to list all attributes and methods of a class or instance
- When an instance can have new attributes
- How to inherit a class from another
- How to define a class with multiple base classes
- What the default class every class inherits from is
- How to override a method or attribute inherited from the base class
- Which attributes or methods are available by heritage to subclasses
- The purpose of inheritance
- How and when to use `isinstance`, `issubclass`, `type`, and `super` built-in functions

## Requirements

### Python Scripts

- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- Code should use the `pycodestyle` (version 2.7.*)
- All files must be executable
- The length of files will be tested using `wc`

### Python Test Cases

- Allowed editors: `vi`, `vim`, `emacs`
- All files should end with a new line
- All test files should be inside a folder `tests`
- All test files should be text files (extension: `.txt`)
- All tests should be executed by using this command: `python3 -m doctest ./tests/*`
- All modules should have documentation
- All classes should have documentation
- All functions (inside and outside a class) should have documentation

## Tasks

0. **Lookup** - Write a function that returns the list of available attributes and methods of an object.
1. **My list** - Write a class `MyList` that inherits from `list`.
2. **Exact same object** - Write a function that returns `True` if the object is exactly an instance of the specified class.
3. **Same class or inherit from** - Write a function that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class.
4. **Only sub class of** - Write a function that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class.
5. **Geometry module** - Write an empty class `BaseGeometry`.
6. **Improve Geometry** - Write a class `BaseGeometry` (based on 5-base_geometry.py).
7. **Integer validator** - Write a class `BaseGeometry` (based on 6-base_geometry.py).
8. **Rectangle** - Write a class `Rectangle` that inherits from `BaseGeometry` (7-base_geometry.py).
9. **Full rectangle** - Write a class `Rectangle` that inherits from `BaseGeometry` (7-base_geometry.py). (Task based on 8-rectangle.py)
10. **Square #1** - Write a class `Square` that inherits from `Rectangle` (9-rectangle.py).
11. **Square #2** - Write a class `Square` that inherits from `Rectangle` (9-rectangle.py). (Task based on 10-square.py)

## Author

- Guillaume

## Acknowledgments

- Holberton School for providing the project guidelines.
