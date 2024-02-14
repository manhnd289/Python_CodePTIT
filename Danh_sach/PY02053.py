if __name__ == "__main__":
    n = int(input())
    matrix = []
    for _ in range(n):
        matrix.append([int(i) for i in input().strip().split()])
    sum_Up, sum_Down = (0,0)
    for i in range(n):
        for j in range(n):
            if j < n-1-i: sum_Up += matrix[i][j]
            elif j > n-1-i: sum_Down += matrix[i][j]
    k = int(input())
    res = abs(sum_Down - sum_Up)
    print("YES" if res <= k else "NO")
    print(res)