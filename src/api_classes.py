import requests
import json
import time
from abc import ABC, abstractmethod


# 1. Создать абстрактный класс для работы с API сайтов с вакансиями
# 2. Реализовать классы, наследующиеся от абстрактного класса, для работы с конкретными платформами

class GetAPIAbstractClass(ABC):

    @abstractmethod
    def get_vacancies(self, vacation_name):  # Метод для получения вакансий с сайта по API
        pass

    @abstractmethod
    def save_vacancies_json_file(self):  # Метод для сохранения полученных данных в файл json
        pass


# Дочерний класс от GetAPIAbstractClass - HeadHunterAPI
class HeadHunterAPI(GetAPIAbstractClass):

    # Инициализация класса
    def __init__(self):
        self.api_data = ''
        self.required_vacation = ''

    # Переопределение метода str, выводим имя родительского класса и запрос пользователя
    def __str__(self):
        return f"{HeadHunterAPI.__name__} считаны данные по запросу: {self.required_vacation}"

    def get_vacancies(self, vacation_name: str) -> None:
        """
        Получение данных с сайта HH по API с запросом
        по вакансии - vacation_name, считываем максимальное
        количество страниц и собираем их в список json_data_list
        :param vacation_name: запрос пользователя (str)
        """
        self.required_vacation = vacation_name
        json_data_list = []
        for pages in range(0, 1):

            params = {
                'text': vacation_name,
                'area': 113,
                'page': pages,
                'per_page': 100
            }
            recs = requests.get("https://api.hh.ru/vacancies", params)
            rec1 = json.loads(recs.content.decode())
            json_data_list.append(rec1)
            if (rec1['pages'] - pages) <= 1:
                break
            time.sleep(0.20)
        self.api_data = json_data_list
        #print(self.api_data)

    def save_vacancies_json_file(self) -> None:
        with open('hh_api.json', 'w', encoding="utf-8") as jsonfile:
            json.dump(self.api_data, jsonfile, ensure_ascii=False)


class SuperJobAPI(GetAPIAbstractClass):

    # Инициализация класса
    def __init__(self):
        self.api_data = ''
        self.required_vacation = ''

    def get_vacancies(self, vacation_name: str) -> None:
        pass

    def save_vacancies_json_file(self) -> None:
        pass



#ap1 = HeadHunterAPI()
#ap1.get_vacancies('python')
#ap1.save_vacancies_json_file()
#print(ap1)

