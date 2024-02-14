while True:
    inp = input()
    if inp == "0 0 0 0": break
    arr = [int(i) for i in inp.split()]
    cnt = 0
    while not(arr[0] == arr[1] and arr[1] == arr[2] and arr[2] == arr[3]):
        tmp = arr[0]
        for i in range(4):
            if i != 3: arr[i] = abs(arr[i] - arr[i+1])
            else: arr[i] = abs(arr[i] - tmp)
        cnt += 1
    print(cnt)

