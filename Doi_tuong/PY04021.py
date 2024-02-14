from datetime import datetime

class Gamer:
    def __init__(self, id, name, start, end) -> None:
        self.id = id
        self.name = name
        self.time = datetime.strptime(end, "%H:%M") - datetime.strptime(start, "%H:%M")
        self.time_minutes = self.time.seconds // 60

    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.time_minutes // 60} gio {self.time_minutes % 60} phut"

if __name__ == "__main__":
    arr = []
    for _ in range(int(input())):
        arr.append(Gamer(input(), input(), input(), input()))
    arr.sort(key = lambda item: -item.time_minutes)
    print(*arr, sep = "\n")
