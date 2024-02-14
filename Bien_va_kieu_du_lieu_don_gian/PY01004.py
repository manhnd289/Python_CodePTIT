from math import isqrt

def gcd1(a : int, b : int) -> int:
    if a == 0 or b==0 : return a+b 
    while(a != b):
        if a > b: a-=b
        else: b -= a
    return a

def gcd2(a : int, b : int) -> int:
    while(a*b!=0):
        if a>b: a %= b
        else: b %= a
    return a+b

def gcd3(a:int, b:int) -> int:
    if b==0: return a
    return gcd3(b,a%b)

def gcd4(a:int, b:int) -> int:
    while(b != 0):
        tmp = a%b
        a = b
        b = tmp
    return a

def checknt(n : int) -> bool:
    if n<2 : return False
    for i in range(2, isqrt(n)+1):
        if n % i == 0: return False
    return True

for _ in range(int(input())):
    n = int(input())
    cnt = 0
    for j in range(1,n):
        if gcd4(n,j) == 1: cnt += 1
    print('YES' if checknt(cnt) else 'NO')