import pytest

from src.category import Category
from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


@pytest.fixture
def first_product():
    return Product("Samsung SC4140V3A", "Цвет синий, Мощность 1600", 7376.0, 5)


@pytest.fixture
def second_product():
    return Product("LG VK69662N", "Цвет красный, Мощность 1800", 6999.99, 10)


@pytest.fixture
def for_category():
    return Category(
        name="Бытовая техника",
        description="Пылесосы",
        products=[
            Product("Samsung SC4140V3A", "Цвет синий, Мощность 1600", 7376.0, 5),
            Product("LG VK69662N", "Цвет красный, Мощность 1800", 6999.99, 10),
        ],
    )


@pytest.fixture
def for_category_empty_product():
    return Category(name="Бытовая техника", description="Пылесосы")


@pytest.fixture
def product_1() -> list:
    return [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство не только коммуникации, "
            "но и получение дополнительных функций для удобства жизни",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                }
            ],
        }
    ]


@pytest.fixture
def product_2() -> list:
    return [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство не только коммуникации, "
            "но и получение дополнительных функций для удобства жизни",
            "products": [
                {
                    "name": "Iphone 15",
                    "description": "512GB, Gray space",
                    "price": 210000.0,
                    "quantity": 8,
                }
            ],
        }
    ]


@pytest.fixture
def first_smartphone():
    return Smartphone("Samsung", "256GB", 180000.0, 5, 95.5, "S23", 256, "Серый")


@pytest.fixture
def second_smartphone():
    return Smartphone("Iphone", "512GB", 210000.0, 8, 98.2, "15", 512, "Gray")


@pytest.fixture
def first_lawn_grass():
    return LawnGrass(
        "Газонная трава", "Элитная", 500.0, 20, "Россия", "7 дней", "Зеленый"
    )


@pytest.fixture
def second_lawn_grass():
    return LawnGrass(
        "Газонная трава 2", "Выносливая", 450.0, 15, "США", "5 дней", "Темно-зеленый"
    )
