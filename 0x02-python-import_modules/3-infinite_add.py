#!/usr/bin/python3
def main():
    print(f"{sum(map(int, argv[1:]))}")

if __name__ == "__main__":
    from sys import argv
    main()
