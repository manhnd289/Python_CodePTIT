if __name__ == "__main__":

    n = int(input())
    arr = []
    try:
        while True:
            arr += [int(i) for i in input().split()]
    except EOFError: pass
    pos, odd, even = [0] * len(arr), [], []
    for i in range(0, len(arr)):
        if(arr[i] % 2 == 0): even.append(arr[i])
        else:
            odd.append(arr[i]); pos[i] = 1
    even = sorted(even)
    odd = sorted(odd, reverse=True)
    i,j = (0,0)
    for item in pos:
        if(item == 0): 
            print(even[i], end = " "); i+=1
        else:
            print(odd[j], end = " "); j+=1
    

