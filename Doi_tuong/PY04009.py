class ComplexNum:

    def __init__(self, real, imaginary) -> None:
        self.real = real
        self.imaginary = imaginary
    def __add__(self, other):
        return ComplexNum(self.real + other.real, self.imaginary + other.imaginary)
    def __mul__(self, other):
        real = self.real*other.real - self.imaginary*other.imaginary
        imaginary = self.imaginary*other.real + self.real*other.imaginary
        return ComplexNum(real, imaginary)
    def __str__(self) -> str:
        return f"{self.real}" + (" + " if self.imaginary>0 else " - ") + f"{abs(self.imaginary)}i"

if __name__ == "__main__":

    for _ in range(int(input())):

        a,b,c,d = map(int, input().split())
        num1 = ComplexNum(a,b)
        num2 = ComplexNum(c,d)
        tmp = num1 + num2
        res1 = tmp * num1
        res2 = tmp * tmp
        print(res1, res2, sep = ", ")
        