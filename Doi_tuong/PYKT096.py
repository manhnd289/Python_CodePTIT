class Team:

    arr_Team = []

    def __init__(self, id_Team, team_Name, college_Name) -> None:
        self.id_Team = id_Team
        self.team_Name = team_Name
        self.college_Name = college_Name
        Team.arr_Team.append(self)


class Candidate:

    def __init__(self, id_Can, name_Can, id_Team) -> None:

        self.id_Can = id_Can
        self.name_Can = name_Can
        self.id_Team = id_Team

        for item in Team.arr_Team:
            if self.id_Team == item.id_Team:
                self.Team = item
                break

    def __str__(self) -> str:
        return f"{self.id_Can} {self.name_Can} {self.Team.team_Name} {self.Team.college_Name}"

if __name__ == "__main__":

    for i in range(1, int(input()) + 1):
        Team.arr_Team.append(Team(f"Team{i:02}", input(), input()))

    arr = []
    for i in range(1, int(input())+1):
        arr.append(Candidate(f"C{i:03}", input(), input()))

    print(*sorted(arr, key = lambda x: x.name_Can), sep = "\n")

