if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n,m = map(int, input().split())
        arr = [int(i) for i in input().split()]
        max_num = max(arr)
        negative, positive = [],[]
        for item in arr:
            if(item < 0): negative.append(item)
            else: positive.append(item)
        negative += positive
        print(*negative[:negative.index(max_num)], end = " ")
        print(m, end = " ")
        print(*negative[negative.index(max_num):])
    