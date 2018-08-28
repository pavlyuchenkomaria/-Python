if __name__ == '__main__':
    string = input()
    a = string.find('f')
    if a == -1:
        print(-2)
        raise SystemExit
    s = [a]
    b = string.find('f', a + 1)
    if b == -1:
        print(-1)
        raise SystemExit
    else:
        print(b)
