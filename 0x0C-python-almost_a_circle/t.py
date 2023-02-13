#!/usr/bin/python3
#!/usr/bin/python3
""" 18-main """
from models.rectangle import Rectangle
from models.square import Square
r1 = Rectangle(5, 3)
r2 = Rectangle(5, 2)
r3 = Rectangle(3, 1)
r4 = Rectangle(6, 4)
s1 = Square(5)
s2 = Square(4)
s3 = Square(3)
s4 = Square(10)
Rectangle.draw([r1, r2], [s1, s2, s3, s4])
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
