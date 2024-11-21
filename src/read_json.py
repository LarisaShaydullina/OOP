import json
from json import JSONDecodeError

# from typing import Any
# from src.external_api import currency_conversion


def read_json(path_to_file: str) -> list:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о
    продуктах."""
    try:
        print(f"Получение данных из файла {path_to_file}")
        with open(path_to_file, encoding="utf-8") as products_file:
            try:
                products_json = json.load(products_file)
            except JSONDecodeError:
                print("Ошибка файла с продуктами")
                return []
        if not isinstance(products_json, list):
            print("Список продуктов пуст")
            return []
        print("Список словарей с данными о продуктах")
        return products_json
    except FileNotFoundError:
        print("Файл с продуктами не найден")
        return []
