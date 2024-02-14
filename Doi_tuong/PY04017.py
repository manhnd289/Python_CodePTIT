from datetime import datetime

class Biker:

    def __init__(self, name: str, region: str, start: str) -> None:
        self.name = name
        self.region = region
        self.id = "".join([item[0].upper() for item in self.region.split()]) + "".join([item[0].upper() for item in self.name.split()])
        time = datetime.strptime(start, "%H:%M") - datetime.strptime("6:00", "%H:%M")
        self.speed = 120 / time.seconds * 3600

    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.region} {round(self.speed)} Km/h"

if __name__ == "__main__":
    
    arr_biker = []
    for _ in range(int(input())):
        arr_biker.append(Biker(input(),input(),input()))
    print(*sorted(arr_biker, key = lambda x: -x.speed), sep = "\n")
