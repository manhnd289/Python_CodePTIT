if __name__ == "__main__":

    for _ in range(int(input())):

        n, cnt = int(input()), 0
        arr = sorted([int(i) for i in input().split()])

        for i in range(n-2):
            l, r = i+1, n-1
            while l < r:
                tmp = arr[i] + arr[l] + arr[r]
                if not tmp:
                    cnt += 1
                    l += 1
                elif tmp < 0: l += 1
                else: r -= 1

        print(cnt)
                