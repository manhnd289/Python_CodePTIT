class Rectangle:

    def __init__(self, length: int, width: int, cl: str ) -> None:
        self.length = length
        self.width = width
        self.cl = cl.title()

    perimeter = lambda self: (self.length + self.width) * 2
    area = lambda self: self.length * self.width
    color = lambda self: self.cl

try: 
    if __name__ == '__main__':
        arr = input().split()
        r = Rectangle(int(arr[0]), int(arr[1]), int(arr[2]))
except:
    if int(arr[0]) > 0 and int(arr[1]) > 0:
        r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
        print("{} {} {}".format(r.perimeter(), r.area(), r.color()))
    else: print("INVALID")