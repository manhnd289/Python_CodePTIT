if __name__ == "__main__":
    inp = input()
    if int(inp) > -10 and int(inp) < 10: print("1")
    else:
        res = 0
        while len(inp) > 1:
            inp = str(sum(ord(i) - ord('0') for i in inp))
            res += 1
        print(res)