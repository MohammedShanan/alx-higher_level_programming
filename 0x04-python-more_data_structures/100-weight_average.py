#!/usr/bin/python3
def weight_average(my_list=[]):
    counter1 = 0
    counter2 = 0
    for score, weight in my_list:
        counter1 += score * weight
        counter2 += weight
    return counter1 / counter2 if my_list != [] else 0
