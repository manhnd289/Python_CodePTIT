def Try(i: int, n: int, k: int, arr_name: list, tmp: list):
    for j in range(tmp[i-1]+1, n-k+i+1):
        tmp[i] = j
        if i == k:
            for m in range(1,k+1):
                print(arr_name[tmp[m]-1], end = " ")
            print()
        else: Try(i+1, n, k, arr_name, tmp)

if __name__ == "__main__":

    n,k = map(int, input().split())
    arr_name = sorted(list(set(input().split())))
    tmp = [0]*(k+1)
    n = len(arr_name)

    Try(1, n, k, arr_name, tmp)