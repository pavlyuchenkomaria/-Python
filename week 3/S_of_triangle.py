from math import sqrt

if __name__ == '__main__':
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a + b + c) / 2
    S = sqrt(p * (p - a) * (p - b) * (p - c))
    if S % 1 == 0:
        print(int(S))
    else:
        print('{0:.6f}'.format(S))
