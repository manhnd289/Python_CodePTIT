if __name__ == "__main__":

    for _ in range(int(input())):

        data = input()

        if len(data) <= 100:
            print(data)
        else:
            data = data[:101]
            idx = data.rindex(" ")
            print(data[:idx])
