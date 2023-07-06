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
    def delete_vacancy(self, vacancy_id):
        pass

    @abstractmethod
    def get_vacancy_by_salary(self):
        pass


class JSONSaver(JsonAbstract):
    """
    Инициализация класса JSONSaver
    """
    def __init__(self, vacancies: list):
        self.vacancies = vacancies

    def save_raw_to_json(self) -> None:
        """
        Запись данных от API в файл 'vacancy_data.json'
        :return: -> None
        """
        with open('vacancy_data.json', 'w', encoding='utf-8') as file:
            json.dump(self.vacancies, file, ensure_ascii=False)
            print(f'Вакансии сохранены в файл vacancy_data.json')
        file.close()

    def get_data_from_file(self):
        with open('vacancy_data.json', 'r', encoding='utf-8') as file:
            vacancies_data = json.load(file)
            print(f'Загружено {len(list(vacancies_data))} вакансий из файла vacancy_data.json')
            self.vacancies = vacancies_data
        file.close()

    def save_vacancy_to_json(self) -> list:
        """
        Собираем данные из экземпляров класса Vacancy
        в json и возвращаем списком
        :return: список вакансий json
        """
        vacancy_list = []
        for recs in Vacancy.all:
            vacancy_list.append(recs.get_json_from_vacancy())
            print(f'{len(vacancy_list)} вакансий готовы к сохранению в файл')
        return vacancy_list

    def get_vacancies(self) -> None:
        """
        Статический метод создания экземпляров класса
        Vacancy, инициализируемых данными из файла
        """
        Vacancy.all.clear()
        vacancies_data = self.vacancies
        for it in vacancies_data:
            Vacancy(it['id'], it['name'], it['url'], it['salary_from'], it['salary_to'], it['description'],
                    it['company'], it['api'])

    def delete_vacancy(self, vacancy_id):
        with open('vacancy_data.json', 'r', encoding='utf-8') as file:
            vacancies_data = json.load(file)
        file.close()
        new_data = []
        list_length = len(vacancies_data)
        for vacancy in vacancies_data:
            if vacancy_id != vacancy['id']:
                new_data.append(vacancy)
        with open('vacancy_data.json', 'w', encoding='utf-8') as file:
            json.dump(new_data, file, ensure_ascii=False)
        file.close()
        if list_length == len(new_data):
            print('Запись с таким id не найдена')
        else:
            print('Запись удалена')

    def get_vacancy_by_salary(self):
        with open('vacancy_data.json', 'r', encoding='utf-8') as file:
            vacancies_data = json.load(file)
            self.vacancies = sorted(vacancies_data, key=lambda vacancy: int(vacancy['salary_from']), reverse=True)
        file.close()


ap1 = HeadHunterAPI()
ap1.find_area_id('Москва')  # Выбираем где искать
ap1.get_api_data('python')  # Выбираем что искать
data = ap1.get_vacancies()  # Получаем данные в json формате
js = JSONSaver(data)    # Создаем экземпляр json_saver, сохраняем данные от api в файл
js.save_raw_to_json()
js.get_data_from_file()
#js.get_vacancies()  # Добавляем данные из файла в класс Vacancies
# vac1 = Vacancy('123458', 'Разраб2', 'http:/1.ru', '1000', '10000', 'Оч хорошая, не напряжная такая, сойдет',
                # 'A&B', 'hh.ru')
js.get_vacancy_by_salary()
js.get_vacancies()
for vacs in range(len(Vacancy.all)):    # Вывод всех вакансий
    print(repr(Vacancy.all[vacs]))
js.delete_vacancy('80643834')
# print(js.save_vacancy_to_json())
