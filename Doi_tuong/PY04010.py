from datetime import datetime

class Candidate:

    def __init__(self, name, dob, mark1, mark2, mark3) -> None:
        self.name = name
        self.dob = datetime.strptime(dob, "%d/%m/%Y").strftime("%d/%m/%Y")
        self.sum_mark = mark1 + mark2 + mark3

    def __str__(self) -> str:
        return f"{self.name} {self.dob} {self.sum_mark:.1f}"
    
if __name__ == "__main__":

    print(Candidate(input(), input(), float(input()), float(input()), float(input())))