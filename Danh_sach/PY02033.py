if __name__ == "__main__":

    data = input()
    data = data[:2*(len(data)//2)]
    arr = []
    for i in range(0, len(data), 2):
        if data[i:i+2] not in arr: arr.append(data[i:i+2])
    print(*arr)