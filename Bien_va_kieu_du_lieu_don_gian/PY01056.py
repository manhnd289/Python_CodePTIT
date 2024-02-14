from math import isqrt

def isPrime(n: str) -> bool:
    num = int(n)
    for i in range(2,isqrt(num)+1):
        if num % i == 0:
            return False
    return True

def check(n : str) -> bool:
    _sum = sum(int(i) for i in n)
    if not isPrime(_sum): return False
    for i in range(len(n)):
        if (i+int(n[i]))&1:
            return False
    return True

for _ in range(int(input())):
    print('YES' if check(input()) else 'NO')