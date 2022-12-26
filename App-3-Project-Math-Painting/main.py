import numpy as np
from PIL import Image


class Square:

    def __init__(self, x, y, side, color):
        self.color = color
        self.y = y
        self.x = x
        self.side = side

    def draw(self, canvas):
        canvas.data[self.x:self.x + self.side, self.y: self.y + self.side] = self.color


class Rectangle:

    def __init__(self, x, y, width, height, color):
        self.color = str_to_tup(color)
        self.y = y
        self.x = x
        self.height = height
        self.width = width

    def draw(self, canvas):
        canvas.data[self.x:self.x + self.height, self.y: self.y + self.width] = self.color


def str_to_tup(color):
    return tuple(map(lambda x: int(x), color))


class Canvas:
    """
    Base on which shapes will be drawn
    """

    def __init__(self, width, height, color):
        self.color = color
        self.height = height
        self.width = width
        self.data = np.zeros((self.width, self.height, 3), dtype=np.uint8)
        if color == "white":
            self.data[:] = (255, 255, 255)
        else:
            self.data[:] = (0, 0, 0)

    def create(self, image_path):
        img = Image.fromarray(self.data, "RGB")
        img.save("canvas.jpg")


canvas_width = int(input("Enter canvas width:"))
canvas_height = int(input("Enter canvas height:"))
canvas_color = input("Enter canvas color ( 'white' or 'black')")
canvas = Canvas(canvas_width, canvas_height, canvas_color)

while True:

    option = input("Enter rectangle or square whicheve you want to draw:")

    if option.lower() == "rectangle":
        rx, ry = input("Enter rectangle origin point  (ex. 100,200)").split(",")
        rectangle_width = int(input("Enter rectangle width:"))
        rectangle_height = int(input("Enter rectangle height:"))
        rectangle_color = input("Enter RGB combination (ex. 100,200,155)").split(",")
        rectangle = Rectangle(int(rx), int(ry), rectangle_width, rectangle_height, rectangle_color)
        rectangle.draw(canvas)
    elif option.lower() == "square":
        sx, sy = input("Enter side origin point  (ex. 100,200)").split(",")
        square_side = int(input("Enter square side:"))
        square_color = input("Enter RGB combination (ex. 100,200,155)").split(",")
        square = Square(int(sx), int(sy), square_side, square_color)
        square.draw(canvas)
    elif option.lower() == "quit":
        break

    canvas.create("")
