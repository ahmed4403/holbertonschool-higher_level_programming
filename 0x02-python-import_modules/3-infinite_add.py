#!/usr/bin/python3
import sys


def main():
    pass


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("0")
    else:
        i = 1
        result = 0
        while(i < len(sys.argv)):
            result = result + int(sys.argv[i])
            i = i + 1
        print(result)
    main()
