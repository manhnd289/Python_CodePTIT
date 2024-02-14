for _ in range(int(input())):
    str = input()
    # print( 'YES' if str[0] == str[-2] and str[1] == str[-1] else 'NO')
    print('YES' if str[:2] == str[-2:] else 'NO')