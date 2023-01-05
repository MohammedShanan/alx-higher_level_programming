#!/usr/bin/python3
def main():
    user_input = argv[1:]
    argc = len(user_input)
    if argc == 0:
        print("0 arguments.")
    else:
        print(f"{argc} arguments:")
    for i in range(argc):
        print(f"{i + 1}: {user_input[i]}")


if __name__ == "__main__":
    from sys import argv
    main()
