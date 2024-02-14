from math import gcd

n,k = map(int, input().split())
res = []
cnt = 0
for val in range(10**(k-1), 10**k):
    if(gcd(n,val) == 1): 
        print(val,end = ' ')
        cnt += 1
    if(cnt == 10):
        print()
        cnt = 0

    