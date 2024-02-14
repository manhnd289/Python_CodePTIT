from math import isqrt
def isPrime(n : int) -> bool:
    if n < 2: return False
    for val in range(2, isqrt(n) + 1):
        if n % val == 0:
            return False
    return True

for _ in range(int(input())):
    _sum = sum(int(i) for i in input())
    print('YES' if isPrime(_sum) else 'NO')