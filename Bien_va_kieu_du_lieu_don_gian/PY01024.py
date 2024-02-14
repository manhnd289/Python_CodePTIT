def isAccepted(n : str) -> bool:
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
        if(i != 0 and abs(int(n[i]) - int(n[i-1])) != 2): return False
    return sum%10==0

for _ in range(int(input())):
    _num = input()
    print('YES' if isAccepted(_num) else 'NO')
    