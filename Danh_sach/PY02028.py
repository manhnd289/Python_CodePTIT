import math

def sieve(prime: list):
    for i in range(2, math.isqrt(10**4)+1):
        if prime[i] == 1:
            for j in range(i*i, 10**4+1, i):
                prime[j] = 0

if __name__ == "__main__":

    prime = [1] * (int(10**4)+1)
    prime[0] = prime[1] = 0

    sieve(prime)

    n = int(input())
    arr = [int(i) for i in input().split()]
    mark = [0] * len(arr)
    arr_prime = []
    for i in range(len(arr)):
        if prime[arr[i]] == 1:
            mark[i] = 1
            arr_prime.append(arr[i])
    arr_prime.sort()
    j = 0
    for i in range(len(arr)):
        if mark[i] == 1: 
            print(arr_prime[j], end = " ")
            j += 1
        else: print(arr[i], end = " ")


