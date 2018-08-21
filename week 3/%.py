from math import floor

# if __name__ == '__main__':
#     P = int(input())
#     X = int(input())
#     Y = int(input())
#     deposit = float(X + 0.01 * Y)
#     after_year_deposit = \
#         (1 + 0.01 * P) * deposit
#     after_year_deposit1 = \
#         int(after_year_deposit)
#     after_year_deposit2 = \
#         int((after_year_deposit - int(after_year_deposit)) * 100)
#     print(after_year_deposit, after_year_deposit1, after_year_deposit2)
# # works not in 2nd iteration, idea - don't make floats - ДЕЛАЙ В ЦЕЛЫХ ЧИСЛАХ

if __name__ == '__main__':
    P = int(input())
    X = int(input())
    Y = int(input())
    s = (int((X * 100 + Y) * (100 + P) / 100)) / 100
    s1 = int(s)
    s2 = int(round((s - s1), 2) * 100)
    print(s1, s2)
