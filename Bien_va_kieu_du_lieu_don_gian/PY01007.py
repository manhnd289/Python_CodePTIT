from math import ceil,log

for _ in range(int(input())):
    n,x,m = [float(i) for i in input().split()]
    # print(ceil(log(m/n,x/100+1)))
    print(ceil(log(m/n)/log(1+x/100)))
    # Có công thức

'''for _ in range(int(input())):
    n, x, m = map(float, input().split())
    year = 1
    while(n <= m):
        n += (x/100) * n
        year += 1
    print(year-1)'''