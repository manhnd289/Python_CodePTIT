def check(a:list, b:list, n):
    for i in range(n):
        if(a[i] > b[i]): return False
    return True

for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    a.sort()
    b.sort()
    print("YES" if check(a,b,n) else "NO")
