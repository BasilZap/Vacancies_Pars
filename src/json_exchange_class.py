import json
from abc import ABC, abstractmethod
from src.vacancy_classes import Vacancy
from src.api_classes import HeadHunterAPI


JSON_FILENAME = 'vacancy_data.json'

# 4. Определить абстрактный класс, который обязывает реализовать методы для добавления вакансий в файл,
#     получения данных из файла по указанным критериям и удаления информации о вакансиях.
# 5. Создать класс для сохранения информации о вакансиях в JSON-файл.


class JsonAbstract(ABC):

    @abstractmethod
    def save_raw_to_json(self):
        pass

    def save_vacancy_to_json(self):
        pass

    @abstractmethod
    def delete_vacancy(self):
        pass

    @abstractmethod
    def get_vacancy_by_salary(self):
        pass


class JSONSaver(JsonAbstract):
    """
    Инициализация класса JSONSaver
    """
    def __init__(self, vacancies):
        self.vacancies = vacancies

    def save_raw_to_json(self) -> None:
        """
        Запись данных от API в файл 'vacancy_data.json'
        :return: -> None
        """
        with open('vacancy_data.json', 'w', encoding='utf-8') as file:
            json.dump(self.vacancies, file, ensure_ascii=False)

    def save_vacancy_to_json(self) -> list:
        """
        Собираем данные из экземпляров класса Vacancy
        в json и возвращаем списком
        :return: список вакансий json
        """
        vacancy_list = []
        for recs in Vacancy.all:
            vacancy_list.append(recs.get_json_from_vacancy())
        return vacancy_list

    @staticmethod
    def get_vacancies(filename) -> None:
        """
        Статический метод создания экземпляров класса
        Vacancy, инициализируемых данными из файла
        :param filename: файл с данными
        """
        with open(filename, 'r', encoding='utf-8') as file:
            vacancies_data = json.load(file)
            for it in vacancies_data:
                Vacancy(it['id'], it['name'], it['url'], it['salary_from'], it['salary_to'], it['description'],
                        it['company'], it['api'])
        file.close()

    def delete_vacancy(self):
        pass

    def get_vacancy_by_salary(self):
        pass


ap1 = HeadHunterAPI()
ap1.find_area_id('Москва')  # Выбираем где искать
ap1.get_api_data('python')  # Выбираем что искать
data = ap1.get_vacancies()  # Получаем данные в json формате
js = JSONSaver(data)    # Создаем экземпляр json_saver, сохраняем данные от api в файл
js.get_vacancies(JSON_FILENAME)  # Добавляем данные из файла в класс Vacancies
vac1 = Vacancy('123458', 'Разраб2', 'http:/1.ru', '1000', '10000', 'Оч хорошая, не напряжная такая, сойдет',
               'A&B', 'hh.ru')
#for vacs in range(len(Vacancy.all)):    # Вывод всех вакансий
    #print(repr(Vacancy.all[vacs]))
print(js.save_vacancy_to_json())

