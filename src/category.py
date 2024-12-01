from src.product import Product


class Category:
    name: str
    description: str
    products: list
    count_of_categories = 0
    count_of_products = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.count_of_products += len(products) if products else 0
        Category.count_of_categories += 1

    def add_product(self, product: Product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.count_of_products += 1
        else:
            raise TypeError

    def __str__(self):
        products_in_stock = 0
        for product in self.__products:
            products_in_stock += product.quantity
        return f"{self.name}, количество продуктов: {products_in_stock} шт."

    @property
    def products(self):
        products_str = ""
        for product in self.__products:
            products_str += f"{str(product)}\n"
        return products_str

    @property
    def products_list(self):
        return self.__products
