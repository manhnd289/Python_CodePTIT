if __name__ == "__main__":

    for _ in range(int(input())):

        n,m,k = map(int, input().split())
        arr1 = [int(i) for i in input().split()]
        arr2 = [int(i) for i in input().split()]
        arr3 = [int(i) for i in input().split()]

        i1, i2, i3, exist = 0, 0, 0, False

        while i1 < n and i2 < m and i3 < k:

            if arr1[i1] == arr2[i2] == arr3[i3]:
                print(arr1[i1], end = " ")
                i1 += 1; i2 += 1; i3 += 1 
                exist = True
            elif arr1[i1] < arr2[i2]: i1 += 1
            elif arr2[i2] < arr3[i3]: i2 += 1
            elif arr3[i3] < arr1[i1]: i3 += 1

        print("" if exist else "NO")  

