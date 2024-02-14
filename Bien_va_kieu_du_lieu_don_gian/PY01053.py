def isAccepted(n : str) -> bool:
    _sum = sum(int(i) for i in n)
    return _sum % 3 == 0

for _ in range(int(input())):
    print('YES' if isAccepted(input()) else 'NO')