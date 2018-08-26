
if __name__ == '__main__':
    stroka = input()
    a = stroka.find('f')
    if a == -1:
        raise SystemExit
    s = [a]
    b = stroka.find('f', a + 1)
    if b == -1:
        print(a)
        raise SystemExit
    s.append(b)
    c = stroka.find('f', b + 1)
    if c == -1:
        print(a, b)
        raise SystemExit
    s.append(c)
    stroka1 = stroka[::-1]
    d = len(stroka) - stroka1.find('f') - 1
    if len(s) > 2:
        print(a, d)
