class Product:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"Product(id={self.id}, name='{self.name}')"


class ProductCollection:
    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.products):
            product = self.products[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration


if __name__ == '__main__':
    collection = ProductCollection()
    collection.add(Product(1, "John"))
    collection.add(Product(2, "Jenifer"))
    for product in collection:
        print(product)
