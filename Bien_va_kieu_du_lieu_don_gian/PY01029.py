from math import gcd

for _ in range(int(input())):
    num = input()
    r_num = num[::-1]
    print('YES' if gcd(int(num), int(r_num)) == 1 else 'NO')