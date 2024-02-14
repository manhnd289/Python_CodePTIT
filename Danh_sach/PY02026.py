if __name__ == "__main__":
    n,m = map(int, input().split())
    a = {int(i) for i in input().split()}
    b = {int(i) for i in input().split()}
    sorted(a) ; sorted(b)
    print("YES" if a == b else "NO")
    