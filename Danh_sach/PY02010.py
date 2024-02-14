if __name__ == "__main__":

    while True:
        n = int(input())
        if n == 0: break
        arr = [int(input()) for i in range(n)]
        if min(arr) == max(arr): print("BANG NHAU")
        else: print(min(arr), max(arr), sep = " ")