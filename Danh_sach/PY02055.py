import math

def sieve(prime: list):

    for i in range(2, math.isqrt(1000)+1):
        if prime[i] == 1:
            for j in range(i*i, 1001, i):
                prime[j] = 0



if __name__ == "__main__":

    prime = [1] * (10**3+1)
    prime[0] = prime[1] = 0

    sieve(prime)

    n, m = map(int, input().split())

    matrix = []
    pos = []
    check = False
    max_prime = 0

    for i in range(n):
        data = input().split()
        for j in range(len(data)):
            num = int(data[j])
            if prime[num] == 1:
                if num > max_prime:
                    max_prime = num
                    pos.clear()
                    pos.append(i); pos.append(j)
                elif num == max_prime: pos.append(i); pos.append(j)

    if max_prime == 0: print("NOT FOUND")
    else:
        print(max_prime)
        for i in range(0, len(pos), 2):
            print(f"Vi tri [{pos[i]}][{pos[i+1]}]")

                