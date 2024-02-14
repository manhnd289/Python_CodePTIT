# Thực chất là tìm số trong khoảng [a,n] chia hết cho k
# Tìm số đầu tiên trong sau a trên trục số chia hết cho k
# Tìm số cuối chia hết cho k sau n rồi chạy loop với step = k

a,k,n = map(int, input().split())

left = k - a % k
# left = (int(a/k) + 1) * k - a
# Tăng 1 do cần 1 số sau a
# -a để coi a là gốc tọa độ

# right = n - n % k - a
# right = int(n/k) * k - a
# Làm tròn xuống vì cần 1 số trước n

res = []
while(a + left <= n):
    res.append(left)
    left += k
if(len(res) == 0): print('-1')
else: print(*res)

'''
if(left > right): print('-1')
else:
    for val in range(left, right+1, k):
        print(val,end = ' ')
    print()
'''
