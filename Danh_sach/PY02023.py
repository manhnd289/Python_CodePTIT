def cmp(num: str):
    return sum(int(i) for i in num), int(num)

if __name__ == "__main__":

    for _ in range(int(input())):
        n = int(input())
        arr = input().split()

        arr = sorted(arr, key = cmp)
        print(*arr)