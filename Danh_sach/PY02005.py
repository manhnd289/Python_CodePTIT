if __name__ == "__main__":

    n = int(input())
    arr = [int(i) for i in input().split()]
    cnt = 0

    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if(arr[i] > arr[j]): cnt+= 1

    print(cnt)