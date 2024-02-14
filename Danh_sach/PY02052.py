if __name__ == "__main__":

    arr = []
    n = int(input())
    for _ in range(n):
        arr.append([int(i) for i in input().split()])
    k = int(input())

    sum1, sum2 = 0, 0

    for i in range(n):
        for j in range(n):
            if i > j: sum1 += arr[i][j]
            elif i < j: sum2 += arr[i][j]

    tmp = abs(sum1-sum2)
    print("YES" if tmp <= k else "NO")
    print(tmp)