n,k = map(int, input().split())
lst = sorted(list(set(map(int,input().split()))))

def combinations():
    res = []
    curr_combination = []
    def backTrack(pos):
        # Chặn ở đây khi đủ số lượng thì bắt đầu backtrack lại ví trí trước đó
        if len(curr_combination) == k:
            res.append(tuple(curr_combination[:]))
            '''
            Cần phải thêm 1 bản sao vì list là 1 đối tượng tham chiếu. Nếu thêm trực tiếp thì đó 
            chỉ đơn giản là thêm tham chiếu. Khi đệ quy cần thay đổi trên curr_combination, nếu
            thêm thẳng vào list thì khi quay lui sẽ thay đổi trên phần tử trong result đó, nên 
            cần tạo 1 bản sao rồi mới thêm vào list
            '''
            return
        for i in range(pos, len(lst)+1):
            curr_combination.append(i)
            backTrack(i+1)
            # Đến đây là đã xuất được 1 cấu hình rồi và giờ sẽ xóa đi 1 phần tử back track
            curr_combination.pop()
    backTrack(1)
    return res

res_ = combinations()
for comb in res_:
    for val in comb:
        print(lst[val-1],end = ' ')
    print()
