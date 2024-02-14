def isReversable(num: str):
    i = 0; j = len(num)-1
    while i < j:
        if num[i] != num[j]: return False
        i += 1; j -= 1
    return len(num) >= 2

if __name__ == "__main__":

    n, m = map(int, input().split())

    max_num = 0
    pos = []

    for i in range(n):
        data = input().split()
        for j in range(m):
            if isReversable(data[j]):
                tmp = int(data[j])
                if max_num < tmp: 
                    max_num = tmp
                    pos.clear()
                    pos.append(i); pos.append(j)
                elif tmp == max_num: pos.append(i); pos.append(j) 

    if max_num == 0: print("NOT FOUND")
    else:
        print(max_num)
        for i in range(0, len(pos), 2):
            print(f"Vi tri [{pos[i]}][{pos[i+1]}]")

    