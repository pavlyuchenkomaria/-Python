if __name__ == '__main__':

    a = float(input())
    b = float(input())
    c = float(input())
    d = float(input())
    e = float(input())
    f = float(input())

    if a.is_integer():
        a = int(a)
    if b.is_integer():
        b = int(b)
    if c.is_integer():
        c = int(c)
    if d.is_integer():
        d = int(d)
    if e.is_integer():
        e = int(e)
    if f.is_integer():
        f = int(f)

    if b != 0:
        x = (f * b - d * e) / (b * c - a * d)
        y = (e - a * x) / b
    else:
        y = (a * f - e * c) / (d * a - e * b)
        x = (e - b * y) / a
    if x.is_integer():
        x = int(x)
    if y.is_integer():
        y = int(y)
    print(x, y)
