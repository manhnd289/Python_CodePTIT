import re

def check(num : int) -> bool:
    n = str(num)
    if len(n)%2: return False
    if (n != n[::-1]): return False
    return re.fullmatch('[0,2,4,6,8]+',n)

for _ in range(int(input())):
    num = int(input())
    '''
    for val in range(22, num, 2):
        if(check(val)): print(val, end = ' ')
    print()
    '''
    i = 2
    n = int(str(i) + str(i)[::-1])
    # Bắt đầu là số 22 nên cứ gấp lên rồi check
    # Ép về int để so sánh
    while n<num:
        # Đã kiểm tra xem n còn nằm trong vùng không
        # Kiểm tra nếu chuỗi chưa gấp lên toàn chữ số chẵn không
        if re.fullmatch('[0,2,4,6,8]+',str(i)):
            print(n,end=' ')
        i+=2
        n = int(str(i) + str(i)[::-1])
        # Đoạn này lấy luôn số sẽ gấp lên vòng while tới
        # Ở đây số thuận nghich là luôn đúng
    print()
