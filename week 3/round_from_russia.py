if __name__ == '__main__':
    number = float(input())
    if (number - int(number)) < 0.5:
        print(int(number))
    else:
        print(int(number)+1)
