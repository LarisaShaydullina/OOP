def test_category_init(for_category):
    assert for_category.name == "Бытовая техника"
    assert for_category.description == "Пылесосы"
    assert for_category.count_of_categories == 1
    assert for_category.count_of_products == 2


def test_category_empty_products(for_category_empty_product):
    assert for_category_empty_product.count_of_products == 2
    assert for_category_empty_product.count_of_categories == 2


def test_products_property(for_category):
    assert (
        for_category.products
        == "Samsung SC4140V3A, 7376.0 руб. Остаток: 5 шт.\nLG VK69662N, 6999.99 руб. Остаток: 10 шт.\n"
    )


def test_str_category(for_category):
    assert str(for_category) == "Бытовая техника, количество продуктов: 15 шт."
