import json
from abc import ABC, abstractmethod

# 4. Определить абстрактный класс, который обязывает реализовать методы для добавления вакансий в файл,
#     получения данных из файла по указанным критериям и удаления информации о вакансиях.
# 5. Создать класс для сохранения информации о вакансиях в JSON-файл.


class JsonAbstract(ABC):

    @abstractmethod
    def add_vacancy(self):
        pass

    @abstractmethod
    def delete_vacancy(self):
        pass

    @abstractmethod
    def get_vacancy_by_salary(self):
        pass

    @abstractmethod
    def save_to_json(self):
        pass



