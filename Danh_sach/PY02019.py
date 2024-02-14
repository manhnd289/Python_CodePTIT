import math

if __name__ == "__main__":
    n = int(input())
    arr = [int(i) for i in input().split()]
    arr.sort()
    for i in range(n):
        for j in range(i+1, n):
            if(math.gcd(arr[i], arr[j]) == 1): print(arr[i], arr[j])