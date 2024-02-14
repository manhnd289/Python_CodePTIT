def fact(n : int):
    res = 1
    for i in range(2, n+1):
        res *= i
    return res

for _ in range(int(input())):
    n = input()
    sum = 0
    for item in n:
        sum += fact(int(item))
    print("Yes" if sum == int(n) else "No")