from src.product import Product


def test_product_1_init(product_1: list) -> None:
    for i in product_1:
        for j in i["products"]:
            product1 = Product(j["name"], j["description"], j["price"], j["quantity"])
    assert product1.name == "Samsung Galaxy C23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5


def test_product_2_init(product_2: list) -> None:
    for i in product_2:
        for j in i["products"]:
            product_2 = Product(j["name"], j["description"], j["price"], j["quantity"])
    assert product_2.name == "Iphone 15"
    assert product_2.description == "512GB, Gray space"
    assert product_2.price == 210000.0
    assert product_2.quantity == 8
