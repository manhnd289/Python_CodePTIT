def binToOct(num: str):

    res = 0
    for i in range(len(num)):
        res += int(num[i]) * 2**(len(num)-1-i)
    return str(res)


if __name__ == "__main__":

    num = input()
    if len(num) % 3 != 0:
        num = '0'* (3*(len(num)//3+1) - len(num)) + num
    
    res = ""
    for i in range(0, len(num), 3):
        res += binToOct(num[i:i+3])

    print(res)