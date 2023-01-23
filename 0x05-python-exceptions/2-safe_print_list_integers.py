#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = i = 0
    while i < x:
        try:
            print("{}".format(my_list[i]), end="")
            counter += 1
        except (TypeError, IndexError):
            continue
        i += 1
    print()
    return counter
