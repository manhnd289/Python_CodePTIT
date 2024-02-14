#from math import 

class Customer:
    def __init__(self, id, name, total) -> None:
        self.id = id
        self.name = name
        self.total = total
        self.fee = 0

    def cal(self):
        if self.total >= 0 and self.total <= 50:
            self.fee = round((self.total*100) * 1.02)
        elif self.total >= 51 and self.total <= 100:
            self.fee = round((50*100 + (self.total-50)*150) * 1.03)
        elif self.total > 100:
            self.fee = round((50*100 + 150*50 + 200*(self.total - 100)) * 1.05)

    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.fee}"
    
lst_cust = []
for i in range(int(input())):
    cus = Customer("KH{0:0>2}".format(i+1), input(), -(int(input())-int(input())))
    cus.cal()
    lst_cust.append(cus)
res = sorted(lst_cust, key= lambda x: x.fee,  reverse=True)
print(*res, sep = "\n")