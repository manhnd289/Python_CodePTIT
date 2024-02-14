from datetime import datetime

class Station:

    def __init__(self, id, name, start, end, amount) -> None:
        self.id = id
        self.name = name
        self.time_elapsed = datetime.strptime(end,"%H:%M") - datetime.strptime(start, "%H:%M")
        self.amount = amount

    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.amount * 3600 / self.time_elapsed.seconds:.2f}"
    
if __name__ == "__main__":

    arr_station, arr_name = [], []
    for _ in range(int(input())):
        name, start, end, amount = input(), input(), input(), int(input())
        if name not in arr_name:
            arr_name.append(name)
            arr_station.append(Station(f"T{len(arr_name):02d}", name, start, end, amount))
        else:
            station = arr_station[arr_name.index(name)]
            station.time_elapsed += datetime.strptime(end,"%H:%M") - datetime.strptime(start, "%H:%M")
            station.amount += amount
    print(*arr_station, sep = "\n")