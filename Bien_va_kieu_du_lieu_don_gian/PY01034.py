if __name__ == "__main__":

    for _ in range(int(input())):

        arr = list(input())

        # Tìm vị trí đầu tiên mà tại đó phần tử đứng trước > phần tử đứng sau
        i = len(arr)-2
        while(i >= 0 and arr[i] <= arr[i+1]): i-=1

        # Nếu không tìm được vị trí nào thì đây là dãy tăng dần
        if i==-1:
            print(-1)
            continue

        # Tìm phần tử lớn nhất và nhỏ hơn vị trí vừa tìm hoặc vị trí đó = vị trí trước 
        # với mục đích tìm số lớn nhất
        j = len(arr)-1
        while arr[i] <= arr[j] or arr[j] == arr[j-1]: j-=1
        arr[i], arr[j] = arr[j], arr[i]

        if arr[0] == "0":
            print(-1)
            continue

        print(*arr, sep = "")