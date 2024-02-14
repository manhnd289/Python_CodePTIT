def solve(num : str) -> int:
    _sum = sum(int(num[i]) for i in range(1,len(num),2))
    _pro = 1
    for i in range(0,len(num),2):
        if int(num[i]):
            _pro *= int(num[i])
    return _pro,_sum

for _ in range(int(input())):
    print(*solve(input()))