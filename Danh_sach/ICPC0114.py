from math import isqrt
import re

def isPrime(n: int):
    for i in range(2, isqrt(n)+1):
        if n % i == 0: return False
    return n>2


if __name__ == "__main__":

    for _ in range(int(input())):

        inp1 = input()
        inp2 = int(inp1)

        sum_digit = sum([int(i) for i in inp1])

        if isPrime(inp2) and isPrime(int(inp1[::-1])) and isPrime(sum_digit) and re.fullmatch("[2357]+", inp1):
            print("Yes")
        else: print("No")