import re
from sys import stdin

if __name__ == "__main__":

    # res = ""
    # inpstr = stdin.readlines()
    # for line in inpstr:
    #     res += re.sub("[\.\?\!]+", "\n", " ".join(re.split("\\s+", line.strip().lower())))
    # for item in re.split("\n\s?", res):
    #     if(item != ""):
    #         print(item[0:1].upper() + item[1:])

    res = " ".join(stdin.readlines()).lower()
    res = re.sub("\\s+", " ", res)
    res = re.split("[\\.\\?\\!] ?", res)
    print(*[i.capitalize() for i in res if i != ""], sep = "\n")

