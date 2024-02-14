n,k = map(int, input().split())
set_ = set(map(int, input().split()))
lst = sorted(list(set_))

tmp = [0] * (k+1)
def Try(i):
    for j in range(tmp[i-1]+1, len(lst)-k+i+1):
        tmp[i] = j
        if i == k:
            for i1 in range(1,k+1):
                print(lst[tmp[i1]-1],end = ' ')
            print()
        else: Try(i+1)
Try(1)


'''
import itertools

n,k = map(int, input().split())
lst = sorted(list(set(map(int,input().split()))))
res = list(itertools.combinations(lst, k))
for val in res:
    print(*val,sep = ' ')
'''