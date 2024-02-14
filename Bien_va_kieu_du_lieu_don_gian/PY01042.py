import re

def check1(n : str) -> bool:
    for val in n:
        if(val != '0' and val != '1' and val != '2'): return False
    return True

def check2(n : str) -> bool:
    return re.fullmatch('[0,1,2]+',n)

def check3(n : str) -> bool:
    return n.count('0') + n.count('1') + n.count('2') == len(n)

for _ in range(int(input())):
    print('YES' if check2(input()) else 'NO')