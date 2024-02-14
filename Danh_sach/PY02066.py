from sys import stdin

if __name__ == "__main__":

    lines = stdin.readlines()

    n = int(lines[0])

    arr = []
    for i in range(1, len(lines)):
        arr += [int(i) for i in lines[i].split()]

    if arr[len(arr)-1] == len(arr): print("Excellent!")
    else:
        for item in range(1, arr[len(arr)-1]):
            if item not in arr: print(item)

