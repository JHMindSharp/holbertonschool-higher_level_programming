# Python - import & modules

## Novice

By: Guillaume

Weight: 1

Your score will be updated as you progress.

### Resources

Read or watch:
- [Modules](https://docs.python.org/3/tutorial/modules.html)
- [Command line arguments](https://docs.python.org/3/tutorial/stdlib.html#command-line-arguments)
- [Pycodestyle – Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
  
man or help:
- `python3`
  
### Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

#### General

- Why Python programming is awesome
- How to import functions from another file
- How to use imported functions
- How to create a module
- How to use the built-in function `dir()`
- How to prevent code in your script from being executed when imported
- How to use command line arguments with your Python programs

### Requirements

#### General

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.*)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using `wc`

### Quiz questions

Great! You've completed the quiz successfully! Keep going!

---

## Tasks

### 0. Import a simple function from a simple file

Write a program that imports the function `def add(a, b):` from the file `add_0.py` and prints the result of the addition `1 + 2 = 3`.

- Use the print function with string format to display integers.
- Assign the value `1` to a variable called `a`.
- Assign the value `2` to a variable called `b`.
- Use those two variables as arguments when calling the functions `add` and `print`.
- `a` and `b` must be defined in 2 different lines: `a = 1` and `b = 2`.
- Your program should print: `<a value> + <b value> = <add(a, b) value>` followed by a new line.
- You can only use the word `add_0` once in your code.
- You are not allowed to use `*` for importing or `__import__`.
- Your code should not be executed when imported.

### 1. My first toolbox!

Write a program that imports functions from the file `calculator_1.py`, does some Maths, and prints the result.

- Do not use the function `print` (with string format to display integers) more than 4 times.
- Define the value `10` to a variable `a`.
- Define the value `5` to a variable `b`.
- Use those two variables only as arguments when calling functions (including `print`).
- `a` and `b` must be defined in 2 different lines: `a = 10` and `b = 5`.
- Your program should call each of the imported functions as shown in the example.
- The word `calculator_1` should be used only once in your file.
- You are not allowed to use `*` for importing or `__import__`.
- Your code should not be executed when imported.

### 2. How to make a script dynamic!

Write a program that prints the number of and the list of its arguments.

- Output should display the number of arguments (with proper grammar) and the list of arguments.
- If no arguments were passed, display a period instead of a colon.
- Your code should not be executed when imported.

### 3. Infinite addition

Write a program that prints the result of the addition of all arguments.

- The output should be the result of the addition of all arguments, followed by a new line.
- You can cast arguments into integers by using `int()`.
- Your code should not be executed when imported.

### 4. Who are you?

Write a program that prints all the names defined by the compiled module `hidden_4.pyc`.

- Print one name per line, in alphabetical order.
- Print only names that do not start with `__`.
- Your code should not be executed when imported.

### 5. Everything can be imported

Write a program that imports the variable `a` from the file `variable_load_5.py` and prints its value.

- You are not allowed to use `*` for importing or `__import__`.
- Your code should not be executed when imported.
