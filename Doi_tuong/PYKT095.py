import re

class Customer:

    @classmethod
    def chuanHoa(cls, name: str):
        name = re.split(r"\s+", name)
        return " ".join(name).title()

    def __init__(self, id, name, data) -> None:
        self.id = id
        self.name = Customer.chuanHoa(name)

        data = data.strip().split()

        if data[0] == "A": self.norm = 100
        elif data[0] == "B": self.norm = 500
        elif data[0] == "C": self.norm = 200

        self.num_elec = int(data[2]) - int(data[1])

        if(self.num_elec < self.norm): 
            self.under_norm = self.num_elec * 450
            self.beyond_norm = 0
        else:
            self.under_norm = self.norm * 450
            self.beyond_norm = (self.num_elec - self.norm) * 1000
        
        self.VAT_tax = int(self.beyond_norm * 0.05)

        self.total_fee = self.under_norm + self.beyond_norm + self.VAT_tax

    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.under_norm} {self.beyond_norm} {self.VAT_tax} {self.total_fee}"

if __name__ == "__main__":

    arr = []

    for i in range(1, int(input())+1):
        arr.append(Customer(f"KH{i:02}", input(), input()))

    print(*sorted(arr, key = lambda x: -x.total_fee), sep = "\n")