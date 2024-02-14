def sieve(arr: list):
    for i in range(10**3):
        if(prime[i] == 1):
            for j in range(i*i, 10**6, i):
                prime[j] = 0

def gcd(a:int, b:int):
    while a*b!=0:
        if a>b: a%=b
        else: b %= a
    return a+b

if __name__ == "__main__":

    prime = [1] * 10**6
    prime[0] = prime[1] = 0
    sieve(prime)

    for _ in range(int(input())):
        a, b = map(int, input().split())
        _gcd = gcd(a,b)
        sum_digit = sum(int(i) for i in str(_gcd))
        print("YES" if prime[sum_digit] == 1 else "NO")