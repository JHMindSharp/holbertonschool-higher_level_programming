#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
if last_digit > 5:
    str_end = ("greater than 5")
elif last_digit == 0:
    str_end = ("0")
elif last_digit < 6 and last_digit != 0:
    str_end = ("less than 6 and not 0")

str = ("Last digit of {} is {} and is {}".format(number, last_digit, str_end))
print(str)
