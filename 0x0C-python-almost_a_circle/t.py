#!/usr/bin/python3
#!/usr/bin/python3
""" 18-main """
from models.rectangle import Rectangle
from models.square import Square

s1 = Square(5)
s2 = Square(7, 9, 1)
list_squares_input = [s1, s2]

Square.save_to_file_csv(list_squares_input)

list_squares_output = Square.load_from_file_csv()

for square in list_squares_input:
    print("[{}] {}".format(id(square), square))

print("---")

for square in list_squares_output:
        print("[{}] {}".format(id(square), square))
