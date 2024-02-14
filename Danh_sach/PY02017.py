if __name__ == "__main__":

    for _ in range(int(input())):

        n = int(input())
        arr = [int(i) for i in input().split()]
        cnt = [0] * 1000005

        res = 0
        for item in arr:
            cnt[item] += 1
            if cnt[item] % 2 == 1:
                res = item
        print(res)
        
