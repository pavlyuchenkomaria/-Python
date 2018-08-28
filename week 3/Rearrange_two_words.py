if __name__ == '__main__':
    string = input()
    pos = string.find(" ")
    print(string[pos + 1:] + " " + string[: pos])
