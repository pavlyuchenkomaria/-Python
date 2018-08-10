a = int(input())
s = a
i = 0
while a != 0:
    a = int(input())
    s += a
    i += 1
print(round((s / i), 11))
# round требует задание