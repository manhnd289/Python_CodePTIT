for _ in range(int(input())):
    n = int(input())
    lst = [int(i) for i in input().split()]

    cnt = dict()
    max_cnt = 0
    min_val = max(lst)
    for item in lst:
        if item in cnt: cnt[item] += 1
        else: cnt[item] = 1
        if max_cnt < cnt[item]: 
            max_cnt = cnt[item]
            min_val = item
        elif max_cnt == cnt[item] and min_val > item: min_val = item
    print(min_val if max_cnt > n/2 else "NO")


