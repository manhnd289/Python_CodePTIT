class Product:

    def __init__(self, id, name, amount, unit_price, discount) -> None:
        self.id = id
        self.name = name
        self.amount = amount
        self.unit_price = unit_price
        self.discount = discount
        self.total_price = unit_price * amount - discount

    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.amount} {self.unit_price} {self.discount} {self.total_price}"


if __name__ == "__main__":

    arr_product = []
    for _ in range(int(input())):
        arr_product.append(Product(input(), input(), int(input()), int(input()), int(input())))
    print(*sorted(arr_product, key = lambda x: -x.total_price), sep = "\n")
