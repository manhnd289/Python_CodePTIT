a = []
while(len(a) < 10):
    a += [int(i) for i in  input().split()]
print(len({i%42 for i in a}))