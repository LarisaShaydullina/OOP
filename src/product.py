# class Product:
#     """Класс продуктов."""
#     name: str
#     description: str
#     price: float
#     quantity: int
#
#
#     def __init__(self, name, description, price, quantity):
#         """Метод для инициализации экземпляра класса."""
#         """Задаем значения атрибутам экземпляра."""
#         self.name = name
#         self.description = description
#         self.price = price
#         self.quantity = quantity


from src.category import Category


class Product(Category):
    """Дочерний класс от Класса категорий: Класс продуктов."""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Метод для инициализации экземпляра класса."""
        """Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
