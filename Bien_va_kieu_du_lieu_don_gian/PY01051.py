for _ in range(int(input())):
    _sum = sum(int(i) for i in input())
    if(_sum <= 9 or str(_sum) != str(_sum)[::-1]): print('NO')
    else: print('YES')