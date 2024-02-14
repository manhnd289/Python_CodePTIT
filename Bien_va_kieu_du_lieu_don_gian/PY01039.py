def check1(n : str) -> bool:
    num_1 = n[0]
    num_2 = n[1]
    if (num_1 == num_2) or n.count(num_1) + n.count(num_2) != len(n): return False
    for i in range(len(n)):
        if (n[i] == num_1 and i%2==1) or (n[i]==num_2 and i%2==0): return False
    return True

def check2(n : str) -> bool:
    if n.count(n[0]) + n.count(n[1]) != len(n): return False
    for i in range(2, len(n), 2):
        if(n[i] != n[i-2]): return False
    for i in range(3, len(n), 2):
        if(n[i] != n[i-2]): return False
    return True

def check3(n : str) -> bool:
    if n[0] == n[1]: return False
    for i in range(2,len(n)):
        if n[i] != n[i & 1]: return False
    return True

for _ in range(int(input())):
    print('YES' if check3(input()) else 'NO')