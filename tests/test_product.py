from src.product import Product


def test_product_init(first_product):
    assert first_product.name == "Samsung SC4140V3A"
    assert first_product.description == "Цвет синий, Мощность 1600"
    assert first_product.price == 7376.0
    assert first_product.quantity == 5


def product_create():
    product = Product("Samsung", "256GB", 10000.0, 5)
    assert product.name == "Samsung"
    assert product.description == "256GB"
    assert product.price == 10000.0
    assert product.quantity == 5


def product_create2():
    product = Product("Колбаса", "Колбаса сыровяленая", 500.0, 10)
    assert product.name == "Колбаса"
    assert product.description == "Колбаса сыровяленая"
    assert product.price == 500.0
    assert product.quantity == 10


def test_product_1_init(product_1: list) -> None:
    for i in product_1:
        for j in i["products"]:
            product5 = Product(j["name"], j["description"], j["price"], j["quantity"])
    assert product5.name == "Samsung Galaxy C23 Ultra"
    assert product5.description == "256GB, Серый цвет, 200MP камера"
    assert product5.price == 180000.0
    assert product5.quantity == 5


def test_product_2_init(product_2: list) -> None:
    for i in product_2:
        for j in i["products"]:
            product_2 = Product(j["name"], j["description"], j["price"], j["quantity"])
    assert product_2.name == "Iphone 15"
    assert product_2.description == "512GB, Gray space"
    assert product_2.price == 210000.0
    assert product_2.quantity == 8


def test_str_product(first_product):
    assert str(first_product) == "Samsung SC4140V3A, 7376.0 руб. Остаток: 5 шт."


def test_add_product(first_product, second_product):
    assert first_product + second_product == 106879.90


def test_price_init(capsys, first_product):
    first_product.price = 0.0
    meesage = capsys.readouterr()
    assert (
        meesage.out.strip().split("\n")[-1]
        == "Цена не должна быть нулевая или отрицательная"
    )

    first_product.price = -1.0
    meesage = capsys.readouterr()
    assert meesage.out.strip() == "Цена не должна быть нулевая или отрицательная"

    first_product.price = -500.0
    meesage = capsys.readouterr()
    assert meesage.out.strip() == "Цена не должна быть нулевая или отрицательная"


def test_price_init3(capsys, first_product):
    first_product.price = 10000
    assert first_product.price == 10000


def test_price_init4(capsys, first_product):
    first_product.price = 9000
    assert first_product.price == 9000
