def check(n : str) -> bool:
    if not len(n)&1 : return False
    if n[0] == n[1]: return False
    for i in range(0, len(n), 2):
        if n[i] != n[0]: return False
    return True

for _ in range(int(input())):
    print('YES' if check(input()) else 'NO')  