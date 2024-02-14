import re

if __name__ == "__main__":

    for _ in range(int(input())):

        n = int(input())
        i = 2
        num = 22
        while num < n:
            if re.fullmatch("^[02468]+$", str(i)):
                print(num, end = " ")
            i += 2
            num = int(str(i) + str(i)[::-1])
        print()