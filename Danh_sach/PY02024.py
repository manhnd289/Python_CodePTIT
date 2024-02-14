def custom_sort(n):
    mul = 1
    for i in str(n):
        mul *= int(i)
    return(mul, n)

lst = [143, 43, 22, 99, 7, 9, 1111, 10]
res = sorted(lst, key = custom_sort)
# res = sorted(lst, key = lambda x: custom_sort(x))
print(*res)