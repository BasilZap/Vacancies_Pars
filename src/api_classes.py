import requests
import json
import time
from abc import ABC, abstractmethod
from src.vacancy_classes import Vacancy


# 1. Создать абстрактный класс для работы с API сайтов с вакансиями
# 2. Реализовать классы, наследующиеся от абстрактного класса, для работы с конкретными платформами

class GetAPIAbstractClass(ABC):

    @abstractmethod
    def get_api_data(self, vacation_name):
        pass

    @abstractmethod
    def get_vacancies(self):  # Метод для получения вакансий с сайта по API
        pass


# Дочерний класс от GetAPIAbstractClass - HeadHunterAPI
class HeadHunterAPI(GetAPIAbstractClass):

    # Инициализация класса
    def __init__(self):
        self.api_data = ''
        self.required_vacation = ''
        self.area = 113

    # Переопределение метода str, выводим имя родительского класса и запрос пользователя
    def __str__(self):
        return f"{HeadHunterAPI.__name__} считаны данные по запросу: {self.required_vacation}"

    def get_api_data(self, vacation_name: str) -> None:
        """
        Получение данных с сайта HH по API с запросом
        по вакансии - vacation_name, считываем максимальное
        количество страниц и собираем их в список json_data_list
        :param vacation_name: запрос пользователя (str)
        """
        self.required_vacation = vacation_name
        json_data_list = []
        for pages in range(0, 20):

            params = {
                'text': vacation_name,
                'host': 'hh.ru',
                'locale': 'RU',
                'area': self.area,
                'page': pages,
                'per_page': 100
            }
            recs = requests.get("https://api.hh.ru/vacancies", params)
            rec1 = json.loads(recs.content.decode())
            json_data_list.extend(rec1['items'])
            if (rec1['pages'] - pages) <= 1:
                break
            print(f'Загрузка страницы - {pages}')
            time.sleep(0.20)
        self.api_data = json_data_list
        print(self.api_data)

    def get_vacancies(self):
        vacation_list = []
        vacancy_counter = 0
        if self.api_data is not None:
            for data in self.api_data:
                v_id = data['id']
                name = data['name']
                link = data['url']
                if data['salary'] is None:
                    salary_from = 0
                    salary_to = 0
                else:
                    if data['salary']['from'] is None:
                        salary_from = 0
                    else:
                        salary_from = data['salary']['from']
                    if data['salary']['to'] is None:
                        salary_to = 0
                    else:
                        salary_to = data['salary']['to']
                if data['snippet']['requirement'] is None:
                    description = ''
                else:
                    description = data['snippet']['requirement']
                company = data['employer']['name']
                api = 'hh.ru'
                vacancy = Vacancy(v_id, name, link, salary_from, salary_to, description, company, api)
                print(repr(vacancy))
                vacancy_counter += 1
                vacation_list.append(vacancy)
        print(f'Загружено {vacancy_counter} вакансий')
        return vacation_list

    def find_area_id(self, area=''):
        rec = requests.get("https://api.hh.ru/areas/113")
        rec1 = json.loads(rec.content.decode())
        # print(rec1)
        if area not in ('', 'Россия'):
            my_str: str = area
            for i in rec1['areas']:
                if i['name'] == str(my_str):
                    self.area = i['id']
                    break
                for y in i['areas']:
                    if y['name'] == str(my_str):
                        self.area = y['id']
                        break
        else:
            self.area = 113


class SuperJobAPI(GetAPIAbstractClass):

    # Инициализация класса
    def __init__(self):
        self.api_data = ''
        self.required_vacation = ''

    def get_api_data(self, vacation_name):
        pass

    def get_vacancies(self) -> None:
        pass










ap1 = HeadHunterAPI()
print(ap1.find_area_id('Москва'))
print(ap1.area)
ap1.get_api_data('python')
ap1.get_vacancies()
#ap1.save_vacancies_json_file()
#print(ap1)

