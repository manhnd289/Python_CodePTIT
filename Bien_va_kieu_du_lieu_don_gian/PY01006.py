for _ in range(int(input())):
    str = input()
    cnt = str.count('4') + str.count('7')
    print('YES' if cnt == str.__len__() else 'NO')

'''for _ in range(int(input())):
    check = True
    for val in input():
        if(val != '4' and val != '7'):
            check = False
            break
    else: print('YES')
    if not check : print('NO')'''
