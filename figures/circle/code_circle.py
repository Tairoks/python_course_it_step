from math import pi

default_radius = 5


def circle_perimeter(r):
    rad = 2 * pi * r
    return round(rad, 2)


def circle_area(r):
    area = pi * r ** 2
    return round(area, 2)

