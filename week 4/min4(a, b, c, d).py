def min4(a, b, c, d):
    min1 = min(a, b)
    min2 = min(c, d)
    min12 = min(min1, min2)
    return min12


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())

    print(min4(a, b, c, d))
