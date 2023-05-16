# CIRCLE
# The goal is to create a class that represents a simple circle_1.
# A Circle can be defined by either specifying the radius or the diameter.
# The user can query the circle_1 for either its radius or diameter.
#
# Other abilities of a Circle instance:
#   - Compute the circle_1’s area
#   - Print the circle_1 and get something nice
#   - Be able to add two circles together
#   - Be able to compare two circles to see which is bigger
#   - Be able to compare two circles and see if there are equal
#   - Be able to put them in a list and sort them

import math


def draw_circle(radius):
    # dist represents distance to the center
    # for horizontal movement
    for i in range((2 * radius) + 1):

        # for vertical movement
        for j in range((2 * radius) + 1):

            dist = math.sqrt((i - radius) * (i - radius) +
                             (j - radius) * (j - radius))

            # dist should be in the
            # range (radius - 0.5)
            # and (radius + 0.5) to print stars(*)
            if radius - 0.5 < dist < radius + 0.5:
                print("*", end=" ")
            else:
                print(" ", end=" ")

        print()


def find_area_radius(r):
    pi = 3.142
    return pi * (r**2)


def find_area_diameter(d):
    pi = 3.142
    return 1/4 * pi * (d**2)


class Circle:

    circles_list = []

    def __init__(self, radius=None, diameter=None):
        if radius:
            self.radius = radius
        elif diameter:
            self.radius = diameter / 2
        else:
            raise ValueError('Must specify either radius or diameter')

        self.circles_list.append(self)

    def compute_area(self):
        return find_area_radius(self.radius)

    def print_circle(self):
        draw_circle(self.radius)

    def sort_circles_list(self):
        self.circles_list.sort(key=lambda x: x.radius, reverse=False)

        return self.circles_list

    def __str__(self):
        return f'Circle with radius {self.radius}'

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(radius=self.radius + other.radius)
        else:
            raise TypeError('Cannot add two circles to each other')

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.radius > other.radius
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius
        else:
            return False


if __name__ == '__main__':
    circle_1 = Circle(radius=2)
    print(circle_1.compute_area())
    circle_1.print_circle()

    circle_2 = Circle(radius=3)

    circle_3 = circle_1 + circle_2
    print(circle_3.radius)
    print(circle_3.compute_area())
    circle_3.print_circle()

    [print(circle.radius) for circle in circle_1.circles_list]

    print(circle_2.sort_circles_list())

    print(circle_1 + circle_2 == circle_3)
    print(circle_1 == circle_2)

    print(circle_1 > circle_2)
    print(circle_3 > circle_2)
    print(circle_3 < circle_2)

