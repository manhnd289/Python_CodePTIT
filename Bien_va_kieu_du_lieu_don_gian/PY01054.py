for _ in range(int(input())):
    num = input()
    _mul = 1
    for val in num:
        if int(val): _mul *= int(val)
    print(_mul)