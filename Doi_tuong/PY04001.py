from math import sqrt

class Point:

    def __init__(self,x: float, y: float) -> None:
        self.x = x
        self.y = y

    def distance(self, p):
        return "{:.4f}".format(sqrt((self.x-p.x)**2 + (self.y-p.y)**2))
    
Decimal = lambda x: float(x)

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1