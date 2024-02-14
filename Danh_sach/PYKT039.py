for _ in range(int(input())):
    n = int(input())
    lst1 = [int(i) for i in input().split()]
    lst2 = [int(i) for i in input().split()]
    lst1.sort()
    lst2.sort()
    check = True
    for i in range(n):
        if lst1[i] > lst2[i]:
            check = False
            break
    print("YES" if check else "NO")