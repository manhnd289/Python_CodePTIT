import re

class Candidate:

    area = [0, 1.5, 1, 0]

    @classmethod
    def chuanHoa(cls, name: str):
        name = re.split("\s+", name.strip())
        return " ". join(name).title()


    def __init__(self, id: str, name: str, mark: float, ethnic: str, region: int) -> None:
        self.id = id
        self.name = Candidate.chuanHoa(name)
        self.priority = 0
        if ethnic != "Kinh": self.priority += 1.5
        self.priority += Candidate.area[region]
        self.final_mark = mark + self.priority
        if self.final_mark >= 20.5: self.status = "Do"
        else: self.status = "Truot"

    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.final_mark} {self.status}"

if __name__ == "__main__":

    arr = []
    for i in range(1, int(input()) + 1):
        arr.append(Candidate(f"TS{i:02}", input(), float(input()), input(), int(input())))
    print(*sorted(arr, key = lambda x: -x.final_mark), sep = "\n")
