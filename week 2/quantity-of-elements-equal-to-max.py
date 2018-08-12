if __name__ == '__main__':
    numbers = []
    number = int(input())
    numbers.append(number)
    max = number
    s = 0
    while number != 0:
        number = int(input())
        numbers.append(number)
        if number >= max:
            max = number
    for number in numbers:
        if number == max:
            s += 1
    print(s)
