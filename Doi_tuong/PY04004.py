def gcd(a: int, b: int):
    while a*b != 0:
        if a>b: a %= b
        else: b %= a
    return a+b

class Fraction:

    def __init__(self, tuSo: int, mauSo: int) -> None:
        _gcd = gcd(tuSo, mauSo)
        self.tuSo = tuSo // _gcd
        self.mauSo = mauSo // _gcd

    def __add__(self, other):
        res_mauSo = (self.mauSo * other.mauSo) // gcd(self.mauSo, other.mauSo)
        res_tuSo = self.tuSo * (res_mauSo // self.mauSo) + other.tuSo * (res_mauSo // other.mauSo)
        return Fraction(res_tuSo, res_mauSo)
    
    def __str__(self) -> str:
        return f"{self.tuSo}/{self.mauSo}"
    
if __name__ == "__main__":

    arr = [int(i) for i in input().split()]
    frac1 = Fraction(arr[0], arr[1])
    frac2 = Fraction(arr[2], arr[3])
    print(frac1 + frac2)
