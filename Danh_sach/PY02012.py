import re

if __name__ == "__main__":
    n = int(input().strip())
    arr = []
    try:
        while True:
            value = [int(i) for i in input().split()]
            arr += value
    except EOFError:
        pass
    pos = []
    le = []
    chan = []
    for i in range(n):
        if arr[i] % 2 == 0: 
            pos.append(1)
            chan.append(arr[i])
        else: 
            pos.append(0)
            le.append(arr[i])
    le.sort()
    k = len(le)-1
    chan.sort()
    j = 0
    for i in range(n):
        if pos[i]==1:
            print(chan[j], end = " ")
            j+=1
        else:
            print(le[k], end = " ")
            k-=1