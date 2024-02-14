import math

if __name__ == "__main__":
    n = int(input())
    arr = []
    res = 0
    for _ in range(n):
        tmp = input()
        tmp1 = tmp.count('C')
        if tmp1 >= 2: res += math.comb(tmp1, 2)
        arr.append(list(tmp))
    for i in range(n):
        cnt = 0
        for j in range(n):
            if(arr[j][i] == "C"): cnt += 1
        if cnt >= 2: res += math.comb(cnt, 2)
    print(res)

    
    