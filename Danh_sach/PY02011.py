if __name__ == "__main__":

    n = int(input())

    arr = [int(i) for i in input().split()]

    step, res = 1e6, 1e6

    for item1 in arr:

        s = sum([abs(item2-item1) for item2 in arr])
        if s < step:
            step = s
            res = item1

    print(step, res, sep = " ")