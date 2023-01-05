#!/usr/bin/python3
def main():
    names = filter(lambda x: not x.startswith('__'), dir(hid4))
    for name in names:
        print(name)


if __name__ == "__main__":
    import hidden_4 as hid4
    main()
