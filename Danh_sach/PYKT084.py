if __name__ == "__main__":
    arr = []
    for _ in range(int(input())):
        tmp = input()
        if tmp == "":
            print(f"{arr[0]}: {len(arr)-1}")
            arr.clear()
        else:
            arr.append(tmp)
    print(f"{arr[0]}: {len(arr)-1}")