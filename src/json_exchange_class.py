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
    def save_raw_to_json(self, vacancies_data):
        pass

    def save_vacancy_to_json(self):
        pass


class JSONSaver(JsonAbstract):
    """
    Инициализация класса JSONSaver
    """
    def __init__(self):
        self.vacancies = []

    def save_raw_to_json(self, vacancies_data) -> None:
        """
        Запись данных от API в файл 'vacancy_data.json'
        :return: -> None
        """
        self.vacancies = vacancies_data
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


#ap1 = HeadHunterAPI()
#ap1.find_area_id('Москва')  # Выбираем где искать
#ap1.get_api_data('python')  # Выбираем что искать
#data = ap1.get_api_vacancy_json_list()  # Получаем данные в json формате
#js = JSONSaver(data)    # Создаем экземпляр json_saver, сохраняем данные от api в файл
#js.save_raw_to_json()
#js.get_data_from_file()
#js.get_vacancies()  # Добавляем данные из файла в класс Vacancies
# vac1 = Vacancy('123458', 'Разраб2', 'http:/1.ru', '1000', '10000', 'Оч хорошая, не напряжная такая, сойдет',
                # 'A&B', 'hh.ru')
#js.get_vacancy_by_salary()
#js.get_vacancies()
#for vacs in range(len(Vacancy.all)):    # Вывод всех вакансий
    #print(repr(Vacancy.all[vacs]))
#js.delete_vacancy('80643834')
# print(js.save_vacancy_to_json())
