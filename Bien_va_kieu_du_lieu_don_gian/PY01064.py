fibo = [0,1]
for i in range(1,26):
    fibo.append(fibo[i]*2+1)

def solve(n: int, k: int):
    if k==fibo[n]//2+1: return n
    elif k > fibo[n]//2+1: return solve(n-1, k-fibo[n-1]-1)
    return solve(n-1, k)

for _ in range(int(input())):
    n,k = map(int, input().split())
    print(chr(solve(n,k) + 64))