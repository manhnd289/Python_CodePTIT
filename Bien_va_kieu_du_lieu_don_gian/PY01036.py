for _ in range(int(input())):
    n = int(input())
    res = sum(1/i for i in range (2-n%2, n+1, 2))
    print('%.6f' % res)

'''
for _ in range(int(input())):
    n = int(input())
    sum = 0
    if(n%2):
        for i in range(1,n+1,2):
            sum += 1/i
    else:
        for i in range(2,n+1,2):
            sum += 1/i
    print('%.6f' % sum)
'''