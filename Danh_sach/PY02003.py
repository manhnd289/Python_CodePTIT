lst = []
MAX = 10**18

def solve():
    i = 1
    while i <= MAX:
        j = 1 
        while j <= MAX:
            k = 1
            while k <= MAX:
                lst.append(i*j*k)
                k*=5
            j*=3
        i*=2
    lst.sort()

def binSearch(l, r, n):
    if l>r: return "Not in sequence"
    mid = (l+r)//2
    if lst[mid] == n: return mid+1
    elif n < lst[mid]: return binSearch(l, mid-1, n)
    return binSearch(mid+1, r, n)

if __name__ == "__main__":

    solve()

    for _ in range(int(input())):
        print(binSearch(0, len(lst), int(input())))
