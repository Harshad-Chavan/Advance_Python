import math
from random import randint

class Point:

    def __init__(self,x, y):
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
        if rectangle.lower_left.x < self.x < rectangle.upper_right.x\
                and rectangle.lower_left.y < self.y < rectangle.upper_right.y:
            return True
        else:
            return False

    def distance(self, point_obj):
        """
        Method to check distance between two points
        :param point_obj:
        :return:
        """
        d = math.sqrt((self.x - point_obj.x)**2 + (self.y - point_obj.y)**2)
        return d

class Rectangle:

    def __init__(self,lower_left_point,upper_right_point):
        """
        Takes points object as parameter
        :param lower_left_point:
        :param upper_right_point:
        """
        self.lower_left = lower_left_point
        self.upper_right = upper_right_point

    def __str__(self):
        return  f"Reactangle corordinates are {self.lower_left.x} , {self.lower_left.y} and {self.upper_right.x}, {self.upper_right.y}"

    def calculate_area(self):
        width = self.upper_right.y - self.lower_left.y
        height = self.upper_right.x - self.lower_left.x
        print(f"calculate area:{width * height}")
        return width * height


if __name__ == "__main__":
    point1 = Point(randint(0,9), randint(0,9))
    point2 = Point(randint(10,19), randint(10,19))

    # create Rectangle object
    rectanglex = Rectangle(point1,point2)
    print(rectanglex)

    user_point = Point(float(input("Guess X:")),float(input("Guess Y:")))

    print(f"Point falls in the rectangle :  {user_point.falls_in_rectangle(rectanglex)}")

    user_area = float(input("Guess Area:"))
    print(f"Your are is of by: {rectanglex.calculate_area() - user_area}")
    # print(pointx.falls_in_rectangle(rectanglex))