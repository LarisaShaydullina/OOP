import json
import os
import pytest
from json import JSONDecodeError

from src.read_json import read_json


@pytest.fixture
def path() -> str:
    PATH_TO_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "products.json")
    return PATH_TO_FILE


@pytest.fixture
def path_empty_list() -> str:
    PATH_TO_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "[]")
    return PATH_TO_FILE



def test_read_json_no_file() -> None:
    assert read_json("no_file") == []


def test_read_json_empty_list(path_empty_list: str) -> None:
    assert read_json(path_empty_list) == []


def test_read_json(path: str) -> None:
    assert read_json(path)[0] == {
    "name": "Смартфоны",
    "description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
    "products": [
        {
            "name": "Samsung Galaxy C23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5
        },
        {
            "name": "Iphone 15",
            "description": "512GB, Gray space",
            "price": 210000.0,
            "quantity": 8
        },
        {
            "name": "Xiaomi Redmi Note 11",
            "description": "1024GB, Синий",
            "price": 31000.0,
            "quantity": 14
        }
    ]
}