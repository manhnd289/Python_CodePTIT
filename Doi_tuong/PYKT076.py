from datetime import datetime

class Film:

    arr_type = {}

    def __init__(self, id, _type, premiere_day, name, num_episode) -> None:
        self.id = id
        self.name = name
        self.premiere_day = datetime.strptime(premiere_day, "%d/%m/%Y")
        self.str_premiere_day= datetime.strftime(self.premiere_day, "%d/%m/%Y")
        self.num_episode = num_episode
        self._type = Film.arr_type[_type]

    def __str__(self) -> str:
        return f"{self.id} {self._type} {self.str_premiere_day} {self.name} {self.num_episode}"

if __name__ == "__main__":
    arr_film = []
    arr_type = {}
    n,m = map(int, input().split())
    for i in range(1, n+1):
        Film.arr_type[f"TL{i:03}"] = input()
    for i in range(1,m+1):
        arr_film.append(Film(f"P{i:03}", input(), input(), input(), int(input())))
    print(*sorted(arr_film, key = lambda x: (x.premiere_day, x.name, -x.num_episode)), sep = "\n")

