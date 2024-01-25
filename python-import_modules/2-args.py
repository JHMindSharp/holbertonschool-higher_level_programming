#!/usr/bin/python3
import sys


def main():
    len_arg = len(sys.argv) - 1
    if len_arg == 0:
        print("{} arguments.".format(len_arg))
    elif len_arg == 1:
        print("{} arguments:".format(len_arg))
    else:
        print("{} arguments:".format(len_arg))

    for i, arg in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(i, arg))


if __name__ == "__main__":
    main()
