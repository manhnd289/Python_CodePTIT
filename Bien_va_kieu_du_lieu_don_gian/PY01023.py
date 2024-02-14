from math import isqrt

# Sử dụng dictionary
def analyze(n : int) -> None:
    res = {}
    for i in range(2, isqrt(n) + 1):
        if not n%i:
            cnt = 0
            while not n%i:
                cnt += 1
                n//=i
            res.update({i : cnt})
    if(n > 1): res.update({n : 1})
    print('1', end = '')
    for i in res:
        print(' * {}^{}'.format(i, res[i]), end='')
    print()

for _ in range(int(input())):
    n = int(input())
    analyze(n)

'''
for _ in range(int(input())):
    n = int(input())
    res = '1 * '
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            cnt = 0
            while(n % i == 0):
                cnt+=1
                n//=i
            res += str(i) + '^' + str(cnt)
            if n!=1: res += ' * '
    if n!=1: res += str(n) + '^1'
    print(res)
'''
