#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def main():
    pass


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(f"Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    num1 = int(sys.argv[1])
    op = sys.argv[2]
    num2 = int(sys.argv[3])
    if op == '+':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif op == '-':
        print(f"{num1} - {num2} = {sub(num1, num2)}")
    elif op == '*':
        print(f"{num1} * {num2} = {mul(num1, num2)}")
    elif op == '/':
        print(f"{num1} / {num2} = {div(num1, num2)}")
    else:
        print(f"Unknown operator. Available operators: +, -, * and /")
        exit(1)
    main()
