import re, math

class Student:

    arr_mark = []

    @classmethod
    def chuanHoa(cls, name: str):
        name = re.split(r"\s+", name.strip())
        return " ".join(name).title()

    def __init__(self, id, name, mark1, mark2, mark3) -> None:
        self.id = id
        self.name = Student.chuanHoa(name)
        self.ave_mark = math.ceil((mark1*3 + mark2*3 + mark3*2) / 8 * 100) / 100
        Student.arr_mark.append(self.ave_mark)

    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.ave_mark:.2f} {Student.arr_mark.index(self.ave_mark)+1}"


if __name__ == "__main__":

    arr = []
    for i in range(1, int(input()) + 1):
        arr.append(Student(f"SV{i:02}", input(), float(input()), float(input()), float(input())))

    Student.arr_mark.sort(reverse=True)
    #print(*Student.arr_mark)
    print(*sorted(arr, key = lambda x: (-x.ave_mark, x.id)), sep = "\n")