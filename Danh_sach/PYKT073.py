if __name__ == "__main__":
    lst = [len(input().split()) for i in range(int(input()))]
    res = []
    i = 0
    while i < len(lst):
        if lst[i] == 7:
            i += 4
            res.append(2)
        elif lst[i] == 6:
            res.append(1)
            i += 2
            while i < len(lst) and lst[i] == 6: i += 2
    print(len(res), *res, sep = "\n")

