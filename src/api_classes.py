import requests
import json
import time
from abc import ABC, abstractmethod

# 1. Создать абстрактный класс для работы с API сайтов с вакансиями
# 2. Реализовать классы, наследующиеся от абстрактного класса, для работы с конкретными платформами


params = {
        'text': 'NAME:Python', # Текст фильтра. В имени должно быть слово "Аналитик"
        'area': 113, # Поиск осуществляется по вакансиям города Москва
        'page': 0, # Индекс страницы поиска на HH
        'per_page': 100 # Кол-во вакансий на 1 странице
    }

rec = requests.get("https://api.hh.ru/vacancies", params)
print(rec)
print(rec.content.decode())
