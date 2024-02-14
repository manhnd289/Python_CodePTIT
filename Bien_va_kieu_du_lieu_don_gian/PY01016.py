for _ in range(int(input())):
    _str = input()
    tmp = ''
    for i in range(0,len(_str), 2):
        tmp += _str[i] * int(_str[i+1])
    print(tmp)



'''
for _ in range(int(input())):
    _str = input()
    for i  in range(0,len(_str),2):
        for _ in range(int(_str[i+1])):
            print(_str[i], end = '')
    print()
'''