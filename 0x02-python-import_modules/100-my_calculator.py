#!/usr/bin/python3
def main():
    ops = {"+": add, "-": sub, "*": mul, "/": div}
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]
    if op in ops:
        print(f"{a} {op} {b} = {ops[op](a,b)}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)


def cal(a, b, op):
    if op == "+":
        return add(a, b)
    elif op == "-":
        return sub(a, b)
    elif op == "*":
        return mul(a, b)
    else:
        return div(a, b)


if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div
    main()
