if __name__ == "__main__":

    n, m = map(int, input().split())

    matrix = []
    max_matrix = 0
    min_matrix = 10**4+5

    for i in range(n):
        matrix.append([int(i) for i in input().split()])
        max_matrix = max(max_matrix, max(matrix[i]))
        min_matrix = min(min_matrix, min(matrix[i]))

    val = max_matrix - min_matrix
    pos = []

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == val:
                pos.append(i); pos.append(j)

    if len(pos) == 0: print("NOT FOUND")
    else:
        print(val)
        for i in range(0, len(pos), 2):
            print(f"Vi tri [{pos[i]}][{pos[i+1]}]")

