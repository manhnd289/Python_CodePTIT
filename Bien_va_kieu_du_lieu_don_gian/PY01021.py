if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        inp = input()
        sum = 0
        _str = ""
        for item in inp:
            if(item.isdigit()): sum += int(item)
            else: _str += item
        print(*sorted(_str),sep = "", end = "")
        print(sum)