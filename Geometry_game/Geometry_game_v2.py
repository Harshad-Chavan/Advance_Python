import math
from random import randint
import turtle


class Point:

    def __init__(self, x, y):
        """
        Constructor
        :param x:
        :param y:
        """
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        """
        Method to check if the point falls in the rectangle
        :param lowleft:
        :param upright:
        :return:
        """
        if rectangle.point_1.x < self.x < rectangle.point_2.x \
                and rectangle.point_1.y < self.y < rectangle.point_2.y:
            return True
        else:
            return False

    def distance(self, point_obj):
        """
        Method to check distance between two points
        :param point_obj:
        :return:
        """
        d = math.sqrt((self.x - point_obj.x) ** 2 + (self.y - point_obj.y) ** 2)
        return d


class Rectangle:

    def __init__(self, point_1, point_2):
        """
        Takes points object as parameter
        :param lower_left_point:
        :param upper_right_point:
        """
        self.point_1 = point_1
        self.point_2 = point_2

    def __str__(self):
        return f"Reactangle corordinates are {self.point_1.x} , {self.point_1.y} and {self.point_2.x}, {self.point_2.y}"

    def calculate_area(self):
        width = self.point_2.y - self.point_1.y
        height = self.point_2.x - self.point_1.x
        print(f"calculate area:{width * height}")
        return width * height


class GuiRectangle(Rectangle):

    def draw_rectangle(self, canvas):
        canvas.penup()
        canvas.goto(self.point_1.x, self.point_1.y)

        canvas.pendown()
        canvas.forward(self.point_2.x - self.point_1.x)
        canvas.left(90)
        canvas.forward(self.point_2.y - self.point_1.y)
        canvas.left(90)
        canvas.forward(self.point_2.x - self.point_1.x)
        canvas.left(90)
        canvas.forward(self.point_2.y - self.point_1.y)
        canvas.left(90)


class GuiPoint(Point):

    def draw_point(self, canvas):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(10, "red")


if __name__ == "__main__":
    point1 = Point(randint(0, 400), randint(0, 400))
    point2 = Point(randint(10, 400), randint(10, 400))

    myturtle = turtle.Turtle()

    # create Rectangle object
    rectanglex = GuiRectangle(point1, point2)

    # Create a user_point on canvas
    user_point = GuiPoint(float(input("Guess X:")), float(input("Guess Y:")))

    print(f"Point falls in the rectangle :  {user_point.falls_in_rectangle(rectanglex)}")

    user_area = float(input("Guess Area:"))
    print(f"Your area is of by: {rectanglex.calculate_area() - user_area}")

    rectanglex.draw_rectangle(canvas=myturtle)
    user_point.draw_point(canvas=myturtle)
    turtle.done()
