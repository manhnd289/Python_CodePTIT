if __name__ == "__main__":

    set1, set2 = set(input().strip().lower().split()), set(input().strip().lower().split())

    print(*sorted(list(set1 | set2)))
    print(*sorted(list(set1 & set2)))