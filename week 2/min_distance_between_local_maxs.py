if __name__ == '__main__':
    n = int(input())
    local_max1 = 0
    local_max2 = 0
    while n != 0:
        n1 = int(input())
        if n1 > n:
            local_max1 = n1
        else:
            local_max1 = local_max1
        n = n1
        n2 = int(input())
        if n2 == 0:
            break
        if n2 > n:
            local_max2 = n2
        else:
            local_max2 = local_max2
        n = n2
    print(local_max1, local_max2)
#task is not ready