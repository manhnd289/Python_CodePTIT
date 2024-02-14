for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    st = []
    for i in range(n):
        while len(st) and a[i] >= a[st[-1]] : st.pop()
        if not len(st): print(i+1, end = " ")
        else: print(i - st[-1], end = " ")
        st.append(i)
    print()
    # Nếu đã pop được đầu stack thì đoạn mà đã pop của cái stack đó cũng pop được
