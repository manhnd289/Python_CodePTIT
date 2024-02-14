def sieve(a: list, prime: list):
    a[0] = a[1] = 0
    for i in range(2, int(10**4+1)):
        if a[i] == 1:
            prime += [i]
            for j in range(i*i, int(10**4 + 1), i):
                a[j] = 0

if __name__ == "__main__":

    a = [1] * int(10**4 + 5)
    prime = []

    sieve(a, prime)

    n = int(input())
    arr = [int(i) for i in input().split()]

    res = 0
    for item1 in arr:
        if a[item1] == 0:
            tmp = min([abs(item1 - item2) for item2 in prime])
            res = max(tmp, res)

    print(res)