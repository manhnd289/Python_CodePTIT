class Student:
    
    def __init__(self, id, name, lop) -> None:
        self.id = id
        self.name = name
        self.lop = lop
        self.mark = 10
        self.status = ""
        
    def getStatus(self, on_class):
        for item in on_class:
            if item == "m": self.mark -= 1
            elif item == "v" : self.mark -= 2
        if self.mark <= 0: 
            self.mark = 0
            self.status = "KDDK"

    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.lop} {self.mark} {self.status}"



if __name__ == "__main__":

    n = int(input())
    arr_sv = []

    for i in range(n):
        arr_sv.append(Student(input(), input(), input()))

    for i in range(n):
        id, data = input().split()
        for item in arr_sv:
            if item.id == id: 
                item.getStatus(data)
                break
    
    print(*arr_sv, sep = "\n")
    