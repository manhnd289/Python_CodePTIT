if __name__ == "__main__":

    n,m = map(int, input().split())
    map = dict()

    for item in input().split():
        map.update({item: 1 if not item in map.keys() else map.get(item)+1})

    map = dict(sorted(map.items(), key = lambda x: (-x[1], x[0])))
    max_cnt = list(map.values())[0]

    check = False
    for k, v in map.items():
        if v < max_cnt:
            print(k)
            check = True
            break
    if not check: print("NONE")

# if __name__ == "__main__":

#     n, m = map(int, input().split())
#     cnt = [0] * (m+1)
#     arr = []
#     max_count = 0
#     for item in input().split():
#         arr.append(int(item))
#         cnt[int(item)] += 1
#         max_count = max(max_count, cnt[int(item)])

#     res = 0
#     for i in range(1, len(cnt)):
#         if(cnt[i] != max_count): res = max(res,cnt[i])
#     print("NONE" if res == 0 else cnt.index(res))
    

# 10 4
# 2 3 1 2 3 4 1 2 3 2
# 3
# 8 4
# 1 2 3 4 4 3 2 1
#NONE