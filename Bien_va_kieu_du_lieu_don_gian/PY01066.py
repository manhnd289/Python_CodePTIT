def check(str_ : str) -> bool:
    str_rev = str_[::-1]
    for i in range(1,len(str_)):
        if abs(ord(str_[i]) - ord(str_[i-1])) != abs(ord(str_rev[i]) - ord(str_rev[i-1])):
            return False
    return True

for _ in range(int(input())):
    print('YES' if check(input()) else 'NO')
