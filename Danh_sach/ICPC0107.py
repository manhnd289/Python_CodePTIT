if __name__ == "__main__":

    for _ in range(int(input())):
        p,q = input().split()
        inp = input().split()
        if len(inp) == 1:
            num1 = inp[0]
            num2 = input()
        else: num1, num2 = inp

        _min = min(p,q) ; _max = max(p,q)

        min1 = int(num1.replace(_max, _min))
        max1 = int(num1.replace(_min, _max))
        min2 = int(num2.replace(_max, _min))
        max2 = int(num2.replace(_min, _max))
        print(min1 + min2, max1 + max2, sep = " ")