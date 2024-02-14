from sys import stdin

class Matrix:

    def __init__(self, row: int, col: int, matrix: list) -> None:
        self.row = row
        self.col = col
        self.matrix = matrix

    def solve(self):

        res = []
        for _ in range(self.row):
            res += [[0] * self.row]

        for i in range(self.row):
            for j in range(self.row):
                for k in range(self.col):
                    res[i][j] += self.matrix[i][k] * self.matrix[j][k]

        return Matrix(self.row, self.row, res)
    
    def __str__(self) -> str:
        for row in self.matrix:
            print(*row)
        return ""

    

if __name__ == "__main__":

    lines = stdin.readlines()
    i = 1
    value = []
    try:
        for line in lines:
            value += [int(i) for i in line.split()]
    except EOFError: pass

    for _ in range(value[0]):
        row, col = value[i], value[i+1]
        i+=2
        matrix = []
        for _ in range(row):
            matrix.append(value[i:i+col])
            i+=col
        print(Matrix(row, col, matrix).solve())

