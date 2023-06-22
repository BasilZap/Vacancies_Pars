import requests
from abc import ABC, abstractmethod

# 1. Создать абстрактный класс для работы с API сайтов с вакансиями
# 2. Реализовать классы, наследующиеся от абстрактного класса, для работы с конкретными платформами

class GetAPIdata(ABC):
