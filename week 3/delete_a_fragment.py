if __name__ == '__main__':
    string = input()
    a = string.find('h')
    reverted_string = string[::-1]
    b = len(string) - reverted_string.find('h') - 1
    print(string[:a] + string[b + 1:])

    output_string = ""
    for i in range(0, a):
        output_string += string[i]
    for i in range(b + 1, len(string)):
        output_string += string[i]
    print(output_string)
