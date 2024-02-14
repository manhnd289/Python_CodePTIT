from math import isqrt

lstPrime = [2,3,5,7]

def isPrime(n : str) -> bool:
    num = int(n)
    if num < 2 : return False
    for i in range(2,isqrt(num)+1):
        if num % i == 0: 
            return False
    return True

def check(n : str) -> bool:
    for i in range(len(n)):
        if (isPrime(i) and int(n[i]) not in lstPrime) or (not isPrime(i) and int(n[i]) in lstPrime):
            return False
    return True

for _ in range(int(input())):
    print('YES' if check(input()) else 'NO')