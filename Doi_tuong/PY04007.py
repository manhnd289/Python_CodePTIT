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

    for _ in range(int(input())):
        row, col = map(int, input().split())
        arr = []
        for _ in range(row):
            arr.append([int(i) for i in input().split()])
        print(Matrix(row, col, arr).solve())
        