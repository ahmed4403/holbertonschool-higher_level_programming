#!/usr/bin/python3
import hidden_4


def main():
    pass


if __name__ == "__main__":
    for string in dir(hidden_4):
        if string[:2] != "__":
            print(f"{string}")
    main()
