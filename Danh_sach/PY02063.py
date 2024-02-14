if __name__ == "__main__":

    n = int(input())
    arr = [int(i) for i in input().split()]

    arr.sort()
    tmp1 = max(arr[-1] * arr[-2] * arr[-3], arr[-1] * arr[-2])
    tmp2 = max(arr[0] * arr[1] * arr[-1], arr[0] * arr[1])
    print(max(tmp1, tmp2))