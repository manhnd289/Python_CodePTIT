class Candidate:

    priority = [0, 2.0, 1.5, 1.0, 0.0]
    subject = {"A":"TOAN", "B":"LY", "C":"HOA"}

    def __init__(self, id, name, id_sub, mark_informatics, mark_specialization) -> None:
        self.name = name
        self.id = id
        self.sub = Candidate.subject[id_sub[0]]
        self.priority = Candidate.priority[int(id_sub[1])]
        self.total_mark = mark_informatics*2 + mark_specialization + self.priority
        if self.total_mark >= 18: self.status = "TRUNG TUYEN"
        else: self.status = "LOAI"

    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.sub} {self.total_mark:.1f} {self.status}"


if __name__ == "__main__":

    arr_candidate = []
    for i in range(1, int(input())+1):
        arr_candidate.append(Candidate(f"GV{i:02}",input(), input(), float(input()), float(input())))
    print(*sorted(arr_candidate, key = lambda x: -x.total_mark), sep = "\n")
