prime_digit = ["2", "3", "5", "7"]
res = []

def check_Num(num: str):
    digits = set(num)
    return len(digits) == 4 and num[-1] != "2"

def backtrack(i, s, n):
    if i >= 4 and i <= n and check_Num(s): res.append(int(s))
    if i < n:
        for item in prime_digit:
            backtrack(i+1, s+item, n)

if __name__ == "__main__":

    backtrack(0, "", int(input()))
    print(*sorted(res), sep = "\n")


