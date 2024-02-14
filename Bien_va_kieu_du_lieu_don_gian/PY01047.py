from math import isqrt

def check(n: str) -> bool:
    num = int(n)
    if num<2: return False
    for val in range(2,isqrt(num)+1):
        if num%val==0: return False
    return True

for _ in range(int(input())):
    num = input()
    print('YES' if check(num[len(num)-4:]) else 'NO')