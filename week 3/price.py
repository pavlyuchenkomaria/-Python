if __name__ == '__main__':
    price = float(input())
    price1 = int(price)
    price2 = int(round(price - int(price), 2) * 100)
    print(price1, price2)
