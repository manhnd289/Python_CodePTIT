str = input()
cnt = str.count('4') + str.count('7')
print('YES' if cnt == 4 or cnt == 7 else 'NO')

'''
cnt_4 = 0; cnt_7 = 0
for val in input():
    if val == '4': cnt_4 += 1
    elif val == '7': cnt_7 += 1

sum_1 = cnt_4 + cnt_7
print('YES' if sum_1 == 4 or sum_1 == 7 else 'NO')
'''