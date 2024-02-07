# Python - Test-driven development

## Background Context

In this project, we focus on the importance of test-driven development (TDD) and the role it plays in writing robust Python programs. The emphasis is on writing the documentation and tests before starting with the actual code, following the TDD philosophy.

**Instructor:** Guillaume

### Important Notice on Intranet Checks for Python Projects

- Documentation (modules and functions) and tests should be written before any code.
- Intranet checks for Python projects will not be released before their first deadline to encourage a focus on TDD.
- Collaboration on test cases is encouraged to cover all edge cases, but the implementation should be individual.
- Always consider edge cases and do not trust user input.

## Resources

- [doctest — Test interactive Python examples](https://docs.python.org/3/library/doctest.html) (until "26.2.3.7. Warnings" included)
- [doctest – Testing through documentation](https://pymotw.com/3/doctest/)
- [Unit Tests in Python](https://realpython.com/python-testing/)

## Learning Objectives

By the end of this project, you should be able to explain:

- Why Python programming is awesome
- What an interactive test is and why tests are important
- How to write Docstrings to create tests
- How to write documentation for each module and function
- The basic option flags for creating tests
- How to find edge cases

## Requirements

### Python Scripts

- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Code should use the `pycodestyle` (version 2.7.*)
- All files must be executable
- The length of files will be tested using `wc`

### Python Test Cases

- Allowed editors: `vi`, `vim`, `emacs`
- All files should end with a new line
- All test files should be inside a folder `tests`
- All test files should be text files (extension: `.txt`)
- All tests should be executed by using this command: `python3 -m doctest ./tests/*`
- All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All functions should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
- Documentation is not a simple word; it’s a real sentence explaining the purpose of the module, class, or method

## Tasks

### 0. Integers addition

Write a function that adds 2 integers.

- Prototype: `def add_integer(a, b=98):`
- `a` and `b` must be integers or floats, otherwise, raise a `TypeError` exception with the message `a must be an integer` or `b must be an integer`
- `a` and `b` must be first cast to integers if they are float
- Returns an integer: the addition of `a` and `b`
- You are not allowed to import any module

### [Other tasks...]

## Quiz Questions

[Include quiz questions if applicable]

## Author

Guillaume - [GitHub](https://github.com/GuillaumeSalva)

