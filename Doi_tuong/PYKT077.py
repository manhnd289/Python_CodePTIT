from datetime import datetime

class Test_Schedule:

    arr_sub = {}

    def __init__(self, id, id_sub, test_day, test_hour, test_group) -> None:
        self.id = id
        self.id_sub = id_sub
        self.test_day = datetime.strptime(test_day, "%d/%m/%Y")
        self.str_test_day = datetime.strftime(self.test_day, "%d/%m/%Y")
        self.test_hour = datetime.strptime(test_hour, "%H:%M")
        self.str_test_hour = datetime.strftime(self.test_hour, "%H:%M")
        self.test_group = test_group

    def __str__(self) -> str:
        return f"{self.id} {self.id_sub} {Test_Schedule.arr_sub[self.id_sub]} {self.str_test_day} {self.str_test_hour} {self.test_group}"
        

if __name__ == "__main__":

    n,m = map(int, input().split())

    for _ in range(n):
        id, name = input(), input()
        Test_Schedule.arr_sub[id] = name\
    
    arr_schedule = []
    for i in range(1, m+1):
        arr_schedule.append(Test_Schedule(f"T{i:03}", *input().split()))

    print(*sorted(arr_schedule, key = lambda x: (x.test_day, x.test_hour , x.id_sub)), sep = "\n")


    