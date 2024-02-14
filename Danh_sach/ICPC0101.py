if __name__ == "__main__":
    
    n = int(input())
    arr1 = [int(i) for i in input().split()]
    arr2 = []

    for item in arr1:
        if len(arr2) > 0 and (item + arr2[len(arr2)-1]) % 2 == 0:
            arr2.pop()
        else:
            arr2.append(item)
    
    print(len(arr2))