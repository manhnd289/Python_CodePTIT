p = [True] * 10001
p[0] = p[1] = False
for i in range(2, 100):
    if(p[i] == True):
        for j in range(i*i, 10001, i):
            p[j] = False

lst = []
for i in range(2,10001):
    if(p[i] == True):
        lst.append(i)

n, x = map(int, input().split())
print(x, end = ' ')
for i in range(n):
    x += lst[i]
    print(x,end = ' ')