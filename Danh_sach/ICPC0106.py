from math import log2

BASE = '0123456789ABCDEF'
# Cơ số này được áp dụng cho tất cả các hệ
# Do từ bin thì mỗi cơ số lấy log2 phần tử

def BinToOthers(b : int, n : str):
    step = int(log2(b)) # Lấy cơ số coi như bước nhảy
    res = ''
    for i in range(0, len(n), step):
        res += BASE[int(n[i:i+step][::-1],2)]
        # Cắt đủ step phần tử để chuyển về int từ bin
        # Khi tính toán tính từ bên phải mà lại truyền chuỗi đã đảo nên phải đảo lại
        # 10|010|100|010|010|101
    return res[::-1]
    # Nhận được chuỗi từ cuối về do truyền vào chuỗi đảo
    # Nên đảo lại lần nữa

for _ in range(int(input())):
    print(BinToOthers(int(input()), input()[::-1]))
    # Cần dảo chuỗi truyền vào do số mũ các hệ tính từ bên phải
