def isReversable(inp: str):
    i = 0; j = len(inp)-1
    while i<j:
        if inp[i] != inp[j]: return False
        i += 1; j -= 1
    return True

if __name__ == "__main__":

    with open("VANBAN.in", "r") as file:
        lines = file.readlines()

    max_len = 0
    arr = []
    res = []

    for line in lines:
        line = line.split()
        arr += line
        for item in line:
            if isReversable(item):
                if max_len <= len(item) and item not in res:
                    res.append(item)
                    max_len = len(item)

    
    for item in res:
        if(len(item) == max_len):
            print(f"{item} {arr.count(item)}")