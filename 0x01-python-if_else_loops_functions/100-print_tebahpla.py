#!/usr/bin/python3
for i in range(26):
    print(
        "{}".format(chr(ord('z') - i)if i % 2 == 0 else chr(ord('z') - i - 32))\
            , end="")
