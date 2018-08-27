if __name__ == '__main__':
    string = input()
    a = string.find('h')
    reverted_string = string[::-1]
    b = len(string) - reverted_string.find('h') - 1
    print(string[:a] + string[b + 1:])
