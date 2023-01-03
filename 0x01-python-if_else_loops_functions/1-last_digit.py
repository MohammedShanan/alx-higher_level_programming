#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_dig = number % 10
if 0 < last_dig < 6:
    print(f"Last digit of {number} is {last_dig} and is less than 6 and not 0")
elif last_dig > 5:
    print(f"Last digit of {number} is {last_dig} and is greater than 5")
else:
    print(f"Last digit of {number} is 0 and is 0")
