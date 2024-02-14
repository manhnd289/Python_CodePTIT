p = [True] *  1000001
p[0] = p[1] = False
for i in range(2, 1000):
    if(p[i] == True):
        for j in range(i*i , 1000001, i):
            p[j] = False
        
n = int(input())
lst = [int(i) for i in input().split()]
res = []
for item in  lst:
    if p[item] == True and item not in res: res.append(item)

for item in res:
    print(item, lst.count(item),sep = " ")