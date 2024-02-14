cnt_lower = 0; cnt_upper = 0
str = input()
for val in str:
    if val.islower(): cnt_lower += 1
    elif val.isupper(): cnt_upper += 1
print(str.lower() if cnt_lower >= cnt_upper else str.upper())