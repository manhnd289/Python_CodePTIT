def check1(n : str) -> bool:
    if len(n) < 3: return False
    for i in range(1,len(n)-1):
        check1 , check2 = True, True
        for j in range(1,i+1):
            if(ord(n[j]) <= ord(n[j-1])):
                check1 = False
                break
        for k in range(i,len(n)-1):
            if(ord(n[k]) <= ord(n[k+1])):
                check2 = False
                break
        if check1 and check2: return True
    return False

def check2(n : str) -> bool:
    if len(n) < 3: return False
    i = 1
    while i < len(n) and n[i] > n[i-1]: i+=1
    while i < len(n) and n[i] < n[i-1]: i+=1
    return i == len(n)

def check3(n : str) -> bool:
    if len(n) < 3: return False
    up = True
    for i in range(1, len(n)):
        if up and ord(n[i]) <= ord(n[i-1]): up = False
        if not up and ord(n[i]) >= ord(n[i-1]): return False
    return True

for _ in range(int(input())):
    print('YES' if check3(input()) else 'NO')