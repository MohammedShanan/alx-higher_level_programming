#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    return {key:value * 2 for key, value in a_dictionary.items()}

#return dict(zip(a_dictionary.keys(),map(lambda x: a_dictionary[x] * 2, a_dictionary)))
