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
        if isinstance(x1, int):
            x1 = int(x1)
        else:
            x1 = '{0:.6f}'.format((-b - sqrt(d)) / (2 * a))
        if isinstance(x2, int):
            x2 = int(x2)
        else:
            x2 = '{0:.5f}'.format((-b + sqrt(d)) / (2 * a))
        if x1 > x2:
            print(x2, x1)
        elif x1 < x2:
            print(x1, x2)
    elif d == 0:
        x = -b / (2 * a)
        if isinstance(x, int):
            x = int(x)
        else:
            x = '{0:.6f}'.format(-b / (2 * a))
        print(x)

# решение через создание функции
# def solver(a, b, c):
#     if b == 0 and c == 0:
#         return [0]
#     d = b ** 2 - 4 * a * c
#     if d > 0:
#         x1 = (-b - sqrt(d)) / (2 * a)
#         x2 = (-b + sqrt(d)) / (2 * a)
#         return [x1, x2]
#     elif d == 0:
#         x = -b / (2 * a)
#         return [x]

# if __name__ == '__main__':
#     #unittest.main()
#     a = float(input())
#     b = float(input())
#     c = float(input())
#
#     solution = solver(a, b, c)
#     if len(solution) == 0:
#         raise SystemExit
#     elif len(solution) == 1:
#         x = solution[0]
#         if x.is_integer():
#             x = int(x)
#         else:
#             x = '{0:.6f}'.format(-b / (2 * a))
#         print(x)
#     elif len(solution) == 2:
#         x1 = solution[0]
#         x2 = solution[1]
#         if x1.is_integer():
#             x1 = int(x1)
#         else:
#             x1 = '{0:.6f}'.format(x1)
#         if x2.is_integer():
#             x2 = int(x2)
#         else:
#             x2 = '{0:.5f}'.format(x2)
#         if x1 > x2:
#             print(x2, x1)
#         elif x1 < x2:
#             print(x1, x2)
#     else:
#         raise SystemExit