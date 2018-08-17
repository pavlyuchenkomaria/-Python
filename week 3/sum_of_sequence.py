if __name__ == '__main__':
    n = int(input())
    i = 1
    s = 0
    while i <= n:
        s += 1 / (i ** 2)
        i += 1
    if s % 1 == 0:
        print(int(s))
    elif n == 2:
        print(s)
    else:
        print('{0:.5f}'.format(s))
