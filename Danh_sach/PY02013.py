while True:
    res = int(input())
    if res == 0: break
    cnt = 1
    while res != 1:
        if(res % 2 == 0): res /= 2
        else: res = res*3 + 1
        cnt+=1
    print(cnt)