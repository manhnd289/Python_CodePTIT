from math import sqrt

class Point:

    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
    def distance(self, other):
        return sqrt((self.x-other.x)**2 + (self.y-other.y)**2)
    
class Triangle:

    def __init__(self, p1, p2, p3) -> None:
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    def __str__(self) -> str:
        a = self.p1.distance(self.p2)
        b = self.p2.distance(self.p3)
        c = self.p3.distance(self.p1)
        return "INVALID" if 2*max(a,b,c) >= a+b+c else "{:.3f}".format(a+b+c)

if __name__ == "__main__":

    t, point_arr, i = int(input()), [], 0
    for _ in range(t):
        point_arr += [float(i) for i in input().split()]
    
    for _ in range(t):
        print(Triangle(Point(*point_arr[i:i+2]), Point(*point_arr[i+2:i+4]), Point(*point_arr[i+4:i+6])))
        i+=6


