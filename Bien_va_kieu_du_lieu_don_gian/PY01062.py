import re
from math import isqrt

prime = [True] * 505
prime[0] = prime[1] = 0
def sieve():
    for i in (2, isqrt(505) + 1):
        if prime[i]:
            for j in range(i*i, 505, i):
                prime[j] = False
sieve()

def check(n : str) -> bool:
    if not prime[len(num)]: return False
    cnt = 0
    for val in n:
        if prime[int(val)]: cnt += 1
        # re.fullmatch('[2357]+',val)
    return cnt > len(num)-cnt

for _ in range(int(input())):
    num = input()
    print('YES' if check(num) else 'NO' )