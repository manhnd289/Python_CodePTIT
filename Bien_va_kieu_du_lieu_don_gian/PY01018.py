P = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'

while True:
    inp = input().split()
    k = int(inp[0])
    if (not k): break
    _str = inp[1]
    res = ''
    for val in _str:
        i = P.index(val)
        res += P[(i+k) % 28]
    print(res[::-1])
    



