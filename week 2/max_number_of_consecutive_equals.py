if __name__ == '__main__':
    n = int(input())
    if n == 0:
        print(0)
        raise SystemExit
    m = 0
    m_last = 0
    while n != 0:
        n1 = int(input())
        if n == n1:
            m += 1
        elif n != n1 and m >= m_last:
            m_last = m
            m = 0
        else:
            m = 0
        n = n1
    if m_last == 0:
        print(1)
    else:
        print(m_last + 1)
