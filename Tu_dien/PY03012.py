class Student:

    def __init__(self, name, ac_ex, sub_ex) -> None:
        self.name = name
        self.ac_ex = ac_ex
        self.sub_ex = sub_ex

    def __str__(self) -> str:
        return f"{self.name} {self.ac_ex} {self.sub_ex}"

if __name__ == "__main__":

    arr = []
    for _ in range(int(input())):
        arr.append(Student(input(), *map(int, input().split())))

    print(*sorted(arr, key = lambda x: (-x.ac_ex, x.sub_ex, x.name)), sep = "\n")
