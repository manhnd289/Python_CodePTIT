for _ in range(int(input())):
    _str = input() + ' '
    # Với mục đích khi duyệt thì space sẽ khác ký tự cuối
    # Thực hiện line 9
    cnt = 0
    res = ''
    for i in range(len(_str)):
        if i == 0 or _str[i] == _str[i-1] : cnt += 1
        elif _str[i] != _str[i-1]:
            res += str(cnt) + _str[i-1]
            cnt = 1
    print(res)
            
'''
for _ in range(int(input())):
    _str = input()
    res = ''
    tmp = _str[0]
    # Lưu phần tử để đếm
    cnt = 0
    # Phần tử đầu tiên chưa đếm được lần nào
    for val in _str:
        # Nếu còn giống phần tử đã lưu thì tăng đếm
        if(val == tmp):
            cnt += 1
            continue
        # Chỗ này là đã có phần tử khác
        # Lưu lại số lần xuất hiện của phần tử đã lưu trước đó
        res += str(cnt) + tmp
        # Được đếm 1 lần rồi
        cnt = 1
        # Lưu phần tử để đếm khác
        tmp = val
    res += str(cnt) + tmp
    print(res)
'''