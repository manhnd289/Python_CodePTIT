def get_Mark(num: int):
    
    if num in range(3,5): return 2.5
    elif num in range(5,7): return 3.0
    elif num in range(7,10): return 3.5
    elif num in range(10,13): return 4.0
    elif num in range(13,16): return 4.5
    elif num in range(16,20): return 5.0
    elif num in range(20,23): return 5.5
    elif num in range(23,27): return 6.0
    elif num in range(27,30): return 6.5
    elif num in range(30,33): return 7.0
    elif num in range(33,35): return 7.5
    elif num in range(35,37): return 8.0
    elif num in range(37,39): return 8.5
    elif num in range(39,41): return 9.0
    else: return 0

if __name__ == "__main__":

    for _ in range(int(input())):

        arr = input().split()

        mark1 = get_Mark(int(arr[0]))
        mark2 = get_Mark(int(arr[1]))

        final_mark = (mark1 + mark2 + float(arr[2]) + float(arr[3])) / 4

        decimal = final_mark - int(final_mark)
        if decimal >= 0.75: final_mark = int(final_mark) + 1
        elif decimal >= 0.25: final_mark = int(final_mark) + 0.5
        else: final_mark = int(final_mark)

        print(f"{final_mark:.1f}")


        