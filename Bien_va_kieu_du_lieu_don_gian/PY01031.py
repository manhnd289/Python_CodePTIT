arr = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

if __name__ == "__main__":
    tmp = []
    for _ in range(int(input())):
        n, b = map(int, input().split())
        res = ""
        while n >= b:
            res += arr[int(n % b)]
            n /= b
        res += arr[int(n % b)]
        res = reversed(res)
        print(*res, sep = "")

    
