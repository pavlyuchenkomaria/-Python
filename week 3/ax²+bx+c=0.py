from math import sqrt

if __name__ == '__main__':
    a = float(input())
    b = float(input())
    c = float(input())
    if a == 0:
        raise SystemExit
    if b == 0 and c == 0:
        print(0)
        raise SystemExit
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = (-b - sqrt(d)) / (2 * a)
        x2 = (-b + sqrt(d)) / (2 * a)
        if abs(x1) >= 1 and x1 % int(x1) == 0:
            x1 = int(x1)
        else:
            x1 = '{0:.6f}'.format((-b - sqrt(d)) / (2 * a))
        if abs(x2) >= 1 and x2 % int(x2) == 0:
            x2 = int(x2)
        else:
            x2 = '{0:.5f}'.format((-b + sqrt(d)) / (2 * a))
        if x1 > x2:
            print(x2, x1)
        elif x1 < x2:
            print(x1, x2)
    elif d == 0:
        x = -b / (2 * a)
        if abs(x) >= 1 and x % int(x) == 0:
            x = int(x)
        else:
            x = '{0:.6f}'.format(-b / (2 * a))
        print(x)
