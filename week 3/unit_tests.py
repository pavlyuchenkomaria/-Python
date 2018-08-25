import unittest
from math import sqrt


def solver(a, b, c):
    if b == 0 and c == 0:
        return [0]
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = (-b - sqrt(d)) / (2 * a)
        x2 = (-b + sqrt(d)) / (2 * a)
        return [x1, x2]
    elif d == 0:
        x = -b / (2 * a)
        return [x]


def format_solution(a, b, c):
    solution = solver(a, b, c)
    if len(solution) == 0:
        raise SystemExit
    elif len(solution) == 1:
        x = solution[0]
        if x.is_integer():
            x = int(x)
        else:
            x = '{0:.6f}'.format(-b / (2 * a))
        return str(x)
    elif len(solution) == 2:
        x1 = solution[0]
        x2 = solution[1]
        if x1.is_integer():
            x1 = int(x1)
        else:
            x1 = '{0:.6f}'.format(x1)
        if x2.is_integer():
            x2 = int(x2)
        else:
            x2 = '{0:.5f}'.format(x2)
        if x1 > x2:
            return str(x2) + ", " + str(x1)
        elif x1 < x2:
            return str(x1) + ", " + str(x2)
    else:
        raise SystemExit


class SolverTests(unittest.TestCase):
    def test_solver(self):
        self.assertEqual(solver(2, 0, 0), [0])
        self.assertEqual(format_solution(1, -1, -2), '-1, 2')
        self.assertEqual(format_solution(1, -7.5, 3), '0.423966, 7.07603')
        self.assertEqual(format_solution(1, 2, 1), '-1')
#  это unit test - тест на проверку конкретной функции или класса функций

if __name__ == '__main__':
    unittest.main()
    a = float(input())
    b = float(input())
    c = float(input())

    print(format_solution(a, b, c))
