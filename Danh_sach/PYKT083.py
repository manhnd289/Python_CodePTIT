from datetime import datetime

class Charge:

    pattern = "%d/%m/%Y"

    def __init__(self, time, total_fee) -> None:
        self.time = datetime.strptime(time, "%d/%m/%Y")
        self.total_fee = total_fee

    def __str__(self) -> str:
        return f"{datetime.strftime(self.time, Charge.pattern)}: {self.total_fee}"
        

if __name__ == "__main__":

    tmp = ""

    fee_table = {"Xe_con 5": 10000, "Xe_con 7": 15000, "Xe_tai 2": 20000, "Xe_khach 29": 50000, "Xe_khach 45": 70000}

    arr = []

    for _ in range(int(input())):

        data = input().strip().split()
        if data[3] == "OUT": continue
        if tmp != data[4]:
            tmp = data[4]
            obj = Charge(tmp, fee_table[data[1] + " " + data[2]])
            arr.append(obj)
        else: obj.total_fee += fee_table[data[1] + " " + data[2]]

    print(*arr, sep = "\n")

