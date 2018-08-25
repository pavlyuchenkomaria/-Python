from math import sqrt

if __name__ == '__main__':
    x = int(input())
    list_of_x = []
    while x != 0:
        list_of_x.append(x)
        x = int(input())
    s = sum(list_of_x) / len(list_of_x)
    sum_of_subtractions = 0
    for x in list_of_x:
        sum_of_subtractions += (x - s) ** 2
    deviation = sqrt(sum_of_subtractions / (len(list_of_x) - 1))
    if deviation.is_integer():
        standart_deviation = deviation
    else:
        standart_deviation = '{0:.11f}'.format(deviation)
    print(standart_deviation)
