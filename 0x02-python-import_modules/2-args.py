#!/usr/bin/python3
import sys


def main():
    pass


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(f"0 arguments.")
    elif len(sys.argv) == 2:
        print(f"1 argument:")
        print(f"1: {sys.argv[1]}")
    else:
        i = 1
        print(f"{len(sys.argv) - 1} arguments:")
        while(i < len(sys.argv)):
            print(f"{i}: {sys.argv[i]}")
            i += 1
    main()
