class Candidate:

    def __init__(self, id, name, practice, theory) -> None:
        self.id = id
        self.name = name
        while theory > 10: theory /= 10
        while practice > 10: practice /= 10
        self.score = (practice + theory) / 2
        if self.score >= 9.5: self.status = "XUAT SAC"
        elif self.score >= 8: self.status = "DAT"
        elif self.score >= 5: self.status = "CAN NHAC"
        else: self.status = "TRUOT"

    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.score:.2f} {self.status}"
    
if __name__ == "__main__":

    arr = []
    for i in range(1, int(input())+1):
        arr.append(Candidate("TS0"+str(i), input(), float(input()), float(input())))

    print(*sorted(arr, key = lambda x: -x.score), sep = "\n")