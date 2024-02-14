class Student:

    def __init__(self, id: str, name: str, mark: list) -> None:
        self.id = id
        self.name = name

        self.ave_mark = round((sum(mark) + mark[0] + mark[1]) / 10 / 1.2, 1)
        if self.ave_mark >= 9: self.status = "XUAT SAC"
        elif self.ave_mark >= 8: self.status = "GIOI"
        elif self.ave_mark >= 7: self.status = "KHA"
        elif self.ave_mark >= 5: self.status = "TB"
        else: self.status = "YEU"

    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.ave_mark:.1f} {self.status}"
    
if __name__ == "__main__":

    arr = []
    for i in range(1, int(input())+1):
        arr.append(Student(f"HS{i:02d}", input(), [float(i) for i in input().split()]))

    print(*sorted(arr, key = lambda x: (-x.ave_mark, x.id)), sep = "\n")