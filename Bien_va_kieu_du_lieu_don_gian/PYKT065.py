from math import isqrt

def isPrime(n: int):
    if n<2: return False
    for i in range(2, isqrt(n)):
        if(n % i == 0): return False
    return True

while(True):
    inp = input()
    if(inp == "-1"): break
    a,b = map(int, inp.split())
    n = int(input())
    cnt = 0
    for i in range(a,b+1):
        if isPrime(i) and i < 2 and i > n: cnt+=1
        elif i%2==0: continue
        else:
            check = True
            for j in range(2,n+1):
                if(i%j==0):
                    check = False
                    break
            if check: cnt += 1
    
    print(cnt)