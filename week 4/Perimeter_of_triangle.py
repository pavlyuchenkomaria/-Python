from math import *


def distance(x1, y1, x2, y2):
    a = (x1 - x2) ** 2
    b = (y1 - y2) ** 2
    dist = sqrt(a + b)
    return dist


if __name__ == '__main__':
    x1 = int(input())
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())
    x3 = int(input())
    y3 = int(input())

    result = distance(x1, y1, x2, y2) + distance(x2, y2, x3,
                                                 y3) + distance(x3,
                                                                y3, x1, y1)
    print(round(result, 10))
