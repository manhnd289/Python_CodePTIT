f = [0,1]
for i in range(2, 93):
        f.append(f[i-2] + f[i-1])

for _ in range(int(input())):
    a,b = map(int, input().split())
    for i in range(a,b+1):
        print(f[i],end = ' ')
    print()
