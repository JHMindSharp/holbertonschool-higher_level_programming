#!/usr/bin/python3
for letter in range(96, 123):
    if letter not in [101, 113]:
        print("{}" .format(chr(letter)), end="")
