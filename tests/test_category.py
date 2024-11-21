from src.category import Category
from src.product import Product


def test_category_1(category_1: Category) -> None:
    assert category_1.name == "Смартфоны"
    assert (
        category_1.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert category_1.category_count == 1
    assert category_1.product_count == 2


def test_category_2() -> None:
    product1 = Product("Samsung", "Smart TV 32 дюйма Full HD с Android TV", 25000.0, 3)
    product2 = Product(
        "Xiaomi", "TV A 50, черный, 4K, 60Гц, Android TV, Smart TV", 32000.0, 2
    )
    category_2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product1, product2],
    )

    assert category_2.name == "Телевизоры"
    assert (
        category_2.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert category_2.category_count == 2
    assert category_2.product_count == 2


def test_category_3(category_3: list) -> None:
    for i in category_3:
        json_category = Category(i["name"], i["description"], i["products"])
    assert json_category.category_count == 4
