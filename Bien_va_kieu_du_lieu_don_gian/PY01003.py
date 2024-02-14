# Xử lý theo int

for _ in range(int(input())):

    arr = list(int(i) for i in input())

    # 1 chữ số thì không cho phép chạm đến phần tử cuối cùng
    # Xét từ cuối về nếu phần tử hiện tại >= 5 thì tăng phần tử trước đó lên 1
    for i in range(-1, -len(arr), -1):
        if arr[i] >= 5:
            arr[i-1] = arr[i-1] + 1
        arr[i] = 0

    # Trường hợp phần tử đầu là 9 bị tăng lên 10
    # Không xử lý vẫn ok vì đây là in ra list
    if arr[0] == 10:
        arr[0] = 0
        arr = [1] + arr

    for val in arr: print(val,end = '')
    print()



'''
Xử lý theo str

def rounded(n : str):
    if(int(n) <= 10) : return n
    
    n = ' '.join(n).split() # List str

    # 9999 vẫn đúng vì so sánh 2 unicode và vẫn gán '0'
    # Chạy xong for sẽ ra :000
    for i in range(len(n)-1, 0, -1):
        if n[i] >= '5':
            n[i-1] = chr(ord(n[i-1]) + 1)
        n[i] = '0'
    print(n)
    
    # Bắt buộc phải xử lý vì đây là mã Unicode không phải int
    # Nếu cứ để xử lý như trên sẽ ra ký tự đặc biệt
    if n[0] > '9' :
        n[0] = '10'
    return ''.join(n)

for _ in range(int(input())):
    print(rounded(input()))
'''