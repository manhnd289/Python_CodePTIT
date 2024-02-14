inp = input()
if len(inp)%3 != 0:
    inp = '0' * (3-(len(inp)%3)) + inp
res = ""
for i in range(0, len(inp), 3):
    res += str(int(inp[i:i+3], 2))
print(res)

