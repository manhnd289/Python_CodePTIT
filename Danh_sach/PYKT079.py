if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = {int(i) for i in input().split()}
        dis = max(arr) - min(arr) + 1
        print(dis - len(arr))