#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 5:
    last_digit = number % -10
else:
    last_digit = number % 10

if last_digit > 5:
    str_end = ("and is greater than 5")
elif last_digit == 0:
    str_end = ("and is 0")
elif last_digit < 6 and last_digit != 0:
    str_end = ("and is less than 6 and not 0")

str = ("Last digit of {} is {} {}".format(number, last_digit, str_end))
print(str)
