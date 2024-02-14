prime = [True] * 10000
prime[0] = prime[1] = False

def sieve():
    for i in range(2, 101):
        if prime[i]:
            for j in range(i*i, 10000, i):
                prime[j] = False

sieve()

for _ in range(int(input())):
    num = input()
    print('YES' if prime[int(num[:3])] and prime[int(num[-3::])] else 'NO')