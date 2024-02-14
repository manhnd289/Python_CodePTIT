from re import findall

a,b,c = map(int, findall(r'\d+', input()))
print('YES' if a+b==c else 'NO')

'''
lst = list(input())
a,b,c = [int(lst[i]) for i in range(0,9,4)]
if a+b == c: print('YES')
else: print('NO')
'''