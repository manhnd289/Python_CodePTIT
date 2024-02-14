for _ in range(int(input())):
    num = input()
    _sum = sum(int(num[i]) for i in range(0,len(num),2))
    _pro = 1
    check = True
    for i in range(1,len(num),2):
        if int(num[i]):
            _pro *= int(num[i])
            check = False
    print(_sum, _pro if not check else '0')
        