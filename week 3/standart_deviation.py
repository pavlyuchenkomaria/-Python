from math import sqrt

if __name__ == '__main__':
    x = int(input())
    S = x
    n = 0
    list_of_x = [x]
    while x != 0:
        x = int(input())
        if x != 0:
            list_of_x.append(x)
        S += x
        n += 1
    s = S / n
    sum_of_subtractions = 0
    for x in list_of_x:
        sum_of_subtractions += (x - s) ** 2
    deviation = sqrt(sum_of_subtractions / (n - 1))
    if deviation.is_integer():
        standart_deviation = deviation
    else:
        standart_deviation = '{0:.11f}'.format(deviation)
    print(standart_deviation)
