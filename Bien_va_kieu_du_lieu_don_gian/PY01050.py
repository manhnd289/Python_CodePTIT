def Try(s, l, a, b, c):
    # Độ dài mỗi lần Try là cố định
    if len(s) == l:
        if a > 0 and a <= b and b <= c:
            print(s)
    else:
        # Nối thêm ký tự và tăng luôn số lượng
        Try(s + 'A', l, a+1, b, c)
        Try(s + 'B', l, a, b+1, c)
        Try(s + 'C', l, a, b, c+1)
for i in range(3,int(input())+1):
    Try('',i,0,0,0)
    # Xử lý theo độ dài, ngắn nhất là 3 ký tự

'''
def isValid(n):
    a = n.count('A')
    b = n.count('B')
    c = n.count('C')
    return a > 0 and a <= b and b <= c

def backTrack(i, s, n, lst):
    if i > n: return
    if isValid(s): lst += [s]
    if i < n: 
        backTrack(i+1, s+'A', n , lst)
        backTrack(i+1, s+'B', n , lst)
        backTrack(i+1, s+'C', n , lst)

lst = []
backTrack(0, '', int(input()), lst)
# Quay lui 1 lần mỗi nhánh sẽ bắt đầu bằng 1 trong 3 ký tự
lst.sort(key = lambda e: (len(e),e))
# Sau khi sinh hết sẽ phải sort
print(*lst,sep='\n')
'''