#!/usr/bin/python3
import sys


def main():
    sum_of_arguments = 0
    for arg in sys.argv[1:]:
        sum_of_arguments += int(arg)
    print("{}".format(sum_of_arguments))


if __name__ == "__main__":
    main()
