#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) is not str:
        return 0
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    i = 0
    while (i < len(roman_string)):
        if (i + 1) < len(roman_string):
            if dic[roman_string[i]] >= dic[roman_string[i + 1]]:
                num += dic[roman_string[i]]
            else:
                num += dic[roman_string[i + 1]] - dic[roman_string[i]]
                i += 2
                continue
        else:
            num += dic[roman_string[i]]
        i += 1
    return num


roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
