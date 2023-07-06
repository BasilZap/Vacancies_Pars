import requests
import os
import json
import time
from abc import ABC, abstractmethod


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
        self.__api_data = ''
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
        for pages in range(0, 1):

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
        self.__api_data = json_data_list
        # print(self.__api_data)

    def get_vacancies(self):
        vacation_list = []
        vacancy_counter = 0
        if self.__api_data is not None:
            for data in self.__api_data:
                vacation_list.append(dict(id=data['id'], name=data['name'], url=data['url']))
                if data['salary'] is None:
                    vacation_list[-1]['salary_from'] = '0'
                    vacation_list[-1]['salary_to'] = '0'
                else:
                    if data['salary']['from'] is None:
                        vacation_list[-1]['salary_from'] = '0'
                    else:
                        vacation_list[-1]['salary_from'] = data['salary']['from']
                    if data['salary']['to'] is None:
                        vacation_list[-1]['salary_to'] = '0'
                    else:
                        vacation_list[-1]['salary_to'] = data['salary']['to']
                if data['snippet']['requirement'] is None:
                    vacation_list[-1]['description'] = ''
                else:
                    vacation_list[-1]['description'] = data['snippet']['requirement']
                vacation_list[-1]['company'] = data['employer']['name']
                vacation_list[-1]['api'] = 'hh.ru'
                # vacancy = Vacancy(v_id, name, link, salary_from, salary_to, description, company, api)
                # print(repr(vacancy))
                vacancy_counter += 1
                # vacation_list.append(vacancy)
                # print(vacation_list[-1])
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
        self.__api_data = ''
        self.required_vacation = ''
        self.area = ''

    def get_api_data(self, vacation_name):
        self.required_vacation = vacation_name
        json_data_list = []
        api_key: str = os.getenv('SJ_API_SECRET_KEY')
        param = {'X-Api-App-Id': api_key}
        for pages in range(0, 5):
            api_request = {
                "keyword": 'SQL',
                "town": "Москва",

                "page": pages,
                "count": 100}
            recs = requests.get('https://api.superjob.ru/2.0/vacancies/',
                                headers=param,
                                params=api_request)
            rec1 = json.loads(recs.content.decode())
            json_data_list.extend(rec1['objects'])
            print(f'Загрузка страницы - {pages}')
            time.sleep(0.20)
        self.__api_data = json_data_list
        print(f'{self.__api_data} \n{len(list(self.__api_data))}')

    def get_vacancies(self) -> None:
        pass


sj = SuperJobAPI()
sj.get_api_data('SQL')

