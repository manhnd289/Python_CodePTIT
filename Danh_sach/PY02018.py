if __name__ == "__main__":
    n = int(input())
    arr = [int(i) for i in input().strip().split()]
    for i in range(1, n+2):
        if not i in arr:
            print(i)
            break
