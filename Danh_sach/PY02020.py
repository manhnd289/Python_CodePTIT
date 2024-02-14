n = int(input())
lst = [float(i) for i in input().split()]
lst.sort()
cnt1, cnt2 = lst.count(lst[0]), lst.count(lst[n-1])
res = 0
for i in range(cnt1, n-cnt2):
    res += lst[i]

res /= n - cnt1 - cnt2
print(f"{res:.2f}")