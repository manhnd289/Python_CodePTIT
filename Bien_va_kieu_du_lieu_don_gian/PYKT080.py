m, n = map(int, input().split())
res = 0

dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]

vs = [[False for j in range(n+2)] for i in range(m+2)]
a = [[0] * (n+2)]
for i in range(m):
    a += [[0] + [int(i) for i in input().split()] + [0]]
a += [[0] * (n+2)]

for i in range(1,m+1):
    for j in range(1,n+1):
        if a[i][j] == -1:
            for k in range(8):
                if not vs[i+dy[k]][j+dx[k]]:
                    res += a[i+dy[k]][j+dx[k]]
                    vs[i+dy[k]][j+dx[k]] = True
            
print(res) 