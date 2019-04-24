class TagCloud:
    def __init__(self):
        self.__tags = {}

    def __len__(self):
        return len(self.__tags)

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower().strip(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower().strip()] = count

    def __iter__(self):
        return iter(self.__tags)

    def add(self, tag):
        tag = tag.lower().strip()
        self.__tags[tag] = self.__tags.get(tag, 0) + 1


cloud = TagCloud()
cloud.add("Python")
cloud.add("python ")
cloud.add("python")
print(len(cloud))

print(cloud.__dict__)


class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Amount must not be less than zero.")
        self.__price = value

    # price = property(get_price, set_price)


product = Product(50)
product.price = -20
print(product.price)
