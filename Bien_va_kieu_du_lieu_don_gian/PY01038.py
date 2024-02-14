rev_num = lambda n: str(n)[::-1]

for _ in range(int(input())):
    num = int(input())
    check = False
    for __ in range(1000):
        if num % 7 == 0:
            check = True
            break
        num += int(rev_num(num))
    else: print('-1')
    if check: print(num)