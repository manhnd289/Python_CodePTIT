from math import isqrt

def isPrime(num : str) -> int:
    n = int(num)
    if n<2 : return 0
    for i in range(2, isqrt(n)+1):
        if n%i==0 : return 0
    return 1

row, col = map(int, input().split())
for i in range(row):
    tmp = list(map(isPrime, input().split()))
    print(*tmp)
    # Unpacking

'''
row, col = map(int, input().split())
matrix = []
for i in range(row):
    matrix.append([int(j) for j in input().split()])
for i in range(row):
    for j in range(col):
        print('1' if isPrime(matrix[i][j]) else '0', end = ' ')
    print()
print()
'''