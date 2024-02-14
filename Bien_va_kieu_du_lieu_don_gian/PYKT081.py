if __name__ == "__main__":

    for _ in range(int(input())):

        arr = input().split('.')

        check = True

        if len(arr) == 4:
            for item in arr:
                if not item.isdigit() or int(item) < 0 or int(item) > 255:
                    check = False
                    break
        else: check = False

        print("YES" if check else "NO")