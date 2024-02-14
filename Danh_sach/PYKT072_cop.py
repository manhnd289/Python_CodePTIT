if __name__ == "__main__":

    n = int(input())
    arr = [input() for i in range(n)]

    res = 10**9
    isValid = True

    for item1 in arr:
        cnt = 0
        for item2 in arr:
            tmp = item2
            for i in range(len(tmp)):
                if tmp == item1:
                    cnt += i
                    break
                tmp = tmp[1:] + tmp[0]
            if item1 != tmp:
                isValid = False
                break
        res = min(res, cnt)
        
    print(-1 if isValid == False else res)
