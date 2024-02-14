from datetime import datetime

class Customer:

    unit_price = [0,25,34,50,80]

    def __init__(self, id, name, id_room, start, end, fee) -> None:
        self.id = id
        self.name = name
        self.id_room = id_room
        self.fee = fee
        time = datetime.strptime(end, "%d/%m/%Y") - datetime.strptime(start, "%d/%m/%Y")
        self.time = time.days + 1
        self.final_price = self.time * Customer.unit_price[int(self.id_room[0])] + self.fee


    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.id_room} {self.time} {self.final_price}"
    

if __name__ == "__main__":
    
    arr_customer = []
    for i in range(1, int(input())+1):
        arr_customer.append(Customer(f"KH{i:02}",input().strip(), input().strip(), input().strip(), input().strip(), int(input().strip())))
    print(*sorted(arr_customer, key = lambda x: -x.final_price), sep = "\n")  
        