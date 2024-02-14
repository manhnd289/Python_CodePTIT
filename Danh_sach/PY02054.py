if __name__ == "__main__":

    row, col = map(int, input().split())

    matrix = []
    for _ in range(row):
        matrix.append([int(i) for i in input().split()])

    if row > col:
        matrix = [matrix[i] for i in range(row) if not(i%2==0 and i//2 < row-col)]
    elif col > row:
        matrix = [[matrix[i][j] for j in range(col) if not(j%2==1 and j//2 < col-row)] for i in range(row)]
    
    for row in matrix:
        print(*row)

# 6 4
# 2 8 7 6
# 6 3 2 6
# 7 2 2 8
# 9 9 9 8
# 9 6 6 3
# 7 7 4 9

# 6 3 2 6
# 9 9 9 8
# 9 6 6 3
# 7 7 4 9

# 4 6
# 2 8 7 6 4 3
# 6 3 2 6 7 2
# 7 2 2 8 9 1
# 9 9 9 8 0 7

# 2 7 4 3
# 6 2 7 2
# 7 2 9 1
# 9 9 0 7