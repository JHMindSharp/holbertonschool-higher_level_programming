#!/usr/bin/python3
import sys


def main():
    arguments = sys.argv
    if len(arguments) == 1:
        num_args = "0 arguments"
        args_list = ""
    else:
        num_args = "{} argument{}".format(
            len(arguments) - 1, "s" if len(arguments) > 2 else ""
        )
        args_list = "\n" + "\n".join(
            ["{}: {}".format(i, arg) for i, arg in enumerate(arguments[1:],
                                                             start=1)]
        )

    print("{}{}{}".format(num_args, "." if len(arguments) == 1 else ":",
                          args_list))


if __name__ == "__main__":
    main()
