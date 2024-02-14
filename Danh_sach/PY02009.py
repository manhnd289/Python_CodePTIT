for _ in range(int(input())):
    n = int(input())
    arr = []
    cnt = dict()
    
    for __ in range(n):
        arr.append(int(input()))
    arr.sort()
    min_val = arr[n-1]
    max_cnt = 0
    for item in arr:
        if item in cnt: cnt[item] += 1
        else: cnt[item] = 1
        if max_cnt < cnt[item]:
            max_cnt = cnt[item]
            min_val = item
    print(min_val)
