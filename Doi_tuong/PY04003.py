def gcd(a: int, b: int):
    while a*b != 0:
        if a>b : a %= b
        else: b %= a
    return a+b

class Fraction:

    def __init__(self, tuSo: int, mauSo: int) -> None:
        _gcd = gcd(tuSo, mauSo)
        self.tuSo = tuSo // _gcd
        self.mauSo = mauSo // _gcd

    def __str__(self) -> str:
        return f"{self.tuSo}/{self.mauSo}"
    
if __name__ == "__main__":

    print(Fraction(*map(int, input().split())))