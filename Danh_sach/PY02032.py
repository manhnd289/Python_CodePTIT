if __name__ == "__main__":

    data = input()
    data = data[:2*(len(data)//2)]
    _set = set()
    for i in range(0,len(data), 2):
        _set.add(data[i:i+2])
    
    print(*sorted(list(_set)), sep = " ")