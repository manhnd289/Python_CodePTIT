if __name__ == "__main__":

    n,m = map(int, input().split())

    arr1 = set([int(i) for i in input().split()])
    arr2 = set([int(i) for i in input().split()])

    print(*sorted(list((arr1.intersection(arr2)))), sep = " ")
    print(*sorted(list((arr1.difference(arr2)))), sep = " ")
    print(*sorted(list((arr2.difference(arr1)))), sep = " ")