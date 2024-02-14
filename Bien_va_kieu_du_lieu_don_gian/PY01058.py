from math import isqrt

def isPrime(n : str) -> bool:
    num = int(n)
    if num<2 : return False
    for i in range(2,isqrt(num)+1):
        if num % i == 0:
            return False
    return True

for _ in range(int(input())):
    print('YES' if isPrime(input()[-4::]) else 'NO')