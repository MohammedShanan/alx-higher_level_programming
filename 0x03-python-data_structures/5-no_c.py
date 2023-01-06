#!/usr/bin/python3
def no_c(my_string):
    return "".join(filter(lambda x: x not in "Cc", my_string))
