# int - округляет в сторону нуля (отбрасывет дробную часть)
# round - округляет до ближайшего целого, если ближайших целых несколько
# (дробная часть равно 0.5), то к чётному
# floor - округляет в меньшую сторону
# ceil - округляет в большую сторону

if __name__ == '__main__':
    a = float(input())
    print(round(a - int(a), 3))