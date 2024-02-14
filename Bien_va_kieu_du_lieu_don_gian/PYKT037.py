lst = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for _ in range(int(input())):
    a,b = map(int, input().split())
    ans = ""
    while a:
        ans += lst[a%b]
        a//=b
    print(ans[::-1])
