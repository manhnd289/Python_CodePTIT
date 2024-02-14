for _ in range(int(input())):
    str = input()
    check = True
    for i in range(1,len(str)-1):
        if(str[i] < str[i-1]):
            check = False
            break
    print('YES' if check else 'NO')
