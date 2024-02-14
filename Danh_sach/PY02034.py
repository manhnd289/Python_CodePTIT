if __name__ == "__main__":

    num = input()
    cnt = [0] * 100
    arr_num = []

    for i in range(0, len(num)-1, 2):
        tmp = int(num[i:i+2])
        if tmp not in arr_num:
            arr_num.append(tmp)
        cnt[tmp] += 1
    
    for item in arr_num:
        print(item, cnt[item], sep = " ")
