for _ in range(int(input())):
    print(input().count(input()))

'''
for _ in range(int(input())):
    str_,num = input(),input()
    cnt,i = 0,0
    while(i < len(str_)):
        if str_[i:i+len(num)] == num: 
            cnt += 1
            i += len(num)
        else: i += 1
    print(cnt)
'''