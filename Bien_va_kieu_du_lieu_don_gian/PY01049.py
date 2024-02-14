from math import isqrt

isPrime = [1]*505
def sieve():
    isPrime[0] = isPrime[1] = 0
    for i in range(2, isqrt(500) + 1):
        if isPrime[i]:
            for j in range(i*2, 500, i):
                isPrime[j] = 0
sieve()

def check(n : str) -> bool:
    if(not isPrime[len(n)]): return False
    cnt_nt = 0
    for val in n:
        if isPrime[int(val)]: cnt_nt+=1
    return cnt_nt > len(n)-cnt_nt

for _ in range(int(input())):
    num = input()
    print('YES' if check(num) else 'NO')

'''
def checknt(n: str) -> bool:
    num = int(n)
    if num < 2: return False
    for val in range(2,isqrt(num)+1):
        if num%val==0: return False
    return True
    
def check(n : str) -> bool:
    if not checknt(str(len(n))): return False
    cnt_nt = 0
    for i in range(len(n)):
        if checknt(n[i]): cnt_nt += 1
    return cnt_nt > len(n) - cnt_nt

for _ in range(int(input())):
    num = input()
    print('YES' if check(num) else 'NO')
'''