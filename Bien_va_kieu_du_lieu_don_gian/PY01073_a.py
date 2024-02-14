def Try(s: str, data: str, check: list):
    if len(s) == len(data):
        print(s)
        return
    for i in range(len(data)):
        if not check[i]:
            check[i] = True
            Try(s + data[i], data, check)
            check[i] = False


if __name__ == "__main__":

    data = input()

    check = [False] * len(data)

    Try("", data, check)

