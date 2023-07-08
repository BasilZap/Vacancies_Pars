# 3. Создать класс для работы с вакансиями, определить атрибуты:
#       - название вакансии
#       - ссылка на вакансию
#       - зарплата
#       - краткое описание/требования

class Vacancy:

    all = []

    def __init__(self, v_id, name, link, salary_from, salary_to, description, company, api):
        self.v_id = v_id
        self.name = name
        self.link = link
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.description = description
        self.company = company
        self.api = api
        self.all = self.all.append(self)

    def __repr__(self):
        """
        Переопределение метода repr
        Вывод полной информации о вакансии
        :return: строка с данными о вакансии
        """
        if self.salary_from == '0':
            salary_from_show = 'не указана'
        else:
            salary_from_show = self.salary_from
        if self.salary_to == '0':
            salary_to_show = 'не указана'
        else:
            salary_to_show = self.salary_to
        desc = self.description
        if len(self.description) > 25:
            desc = self.description[:25] + '...'

        return f"id: {self.v_id}, name: {self.name}, link: {self.link}, " \
               f"salary: {salary_from_show} - {salary_to_show}, " \
               f"description: {desc}, company - {self.company}, api - {self.api}"

    def __str__(self):
        pay = str(self.salary_from) + '-' + str(self.salary_to)
        return f'Вакансия: {self.name} с З/П: {pay} в организацию {self.company}'

    def __eq__(self, other) -> bool:
        """
               =
               :param other:
               :return:
               """
        if self.salary_from == other.salary_from:
            return True
        else:
            return False

    def __lt__(self, other):
        """
        <
        :param other:
        :return:
        """
        if self.salary_from < other.salary_from:
            return True
        else:
            return False

    def __le__(self, other):
        """
        <=
        :param other:
        :return:
        """
        if self.salary_from <= other.salary_from:
            return True
        else:
            return False

    def __gt__(self, other):
        """
        >
        :param other:
        :return:
        """
        if self.salary_from > other.salary_from:
            return True
        else:
            return False

    def __ge__(self, other):
        """
        >=
        :param other:
        :return:
        """
        if self.salary_from >= other.salary_from:
            return True
        else:
            return False

    @classmethod
    def get_json_from_vacancy(cls):
        """
        Класс-метод выгружает данные из экземпляров класса
        Vacancy в формат json
        :return: Список словарей в json
        """
        vacancies_data = []
        for vacancy in cls.all:
            vacancies_data.append({'id': vacancy.v_id, 'name': vacancy.name, 'url': vacancy.link,
                                   'salary_from': vacancy.salary_from, 'salary_to': vacancy.salary_to,
                                   'description': vacancy.description, 'company': vacancy.company, 'api': vacancy.api})

        return vacancies_data

    @classmethod
    def delete_vacancy(cls, element_id):
        """
        Класс-метод поиска и удаления экземпляра класса Vacancy
        по id вакансии
        :param element_id: id эл-та, который необходимо удалить, str
        :return:
        """
        length_of_list = len(cls.all)
        for vacancy in range(len(cls.all)-1):
            if cls.all[vacancy].v_id == element_id:
                print(f'!!!Запись - {repr(cls.all[vacancy])} удалена!!!')
                cls.all.pop(vacancy)
                break
        if length_of_list == len(cls.all):
            print('Запись с таким ID не найдена')


    @classmethod
    def get_vacancies(cls, vacancies_data) -> None:
        """
        Класс-метод создания экземпляров класса
        Vacancy, инициализируемых данными vacancies_data
        """
        cls.all.clear()
        for it in vacancies_data:
            cls(it['id'], it['name'], it['url'], it['salary_from'], it['salary_to'], it['description'],
                it['company'], it['api'])


    @classmethod
    def show_n_vacancies(cls, number_to_show=100000):
        if number_to_show == 100000:
            number_to_show = len(cls.all)-1
        else:
            if number_to_show > len(cls.all)-1:
                print(f"В списке только {len(cls.all)}")
                number_to_show = len(cls.all) - 1
        for numbers in range(number_to_show):
            print(repr(cls.all[numbers]))

    @classmethod
    def add_vacancy(cls, v_id, name, link, salary_from, salary_to, description, company, api="user"):
        cls.all.append(cls(v_id, name, link, salary_from, salary_to, description, company, api))

    @staticmethod
    def vacancy_data_splitter(hh_data: list, sj_data: list):
        all_vacancies = hh_data
        all_vacancies.extend(sj_data)
        return all_vacancies


    @staticmethod
    def get_vacancy_by_salary(vacancies_data):
        """
        Функция сортировки данных вакансий по убыванию начальной з\п
        :param vacancies_data: Список вакансий json
        :return: Список отсортированных вакансий json
        """
        vacancies = sorted(vacancies_data, key=lambda vacancy: int(vacancy['salary_from']), reverse=True)
        return vacancies

#vac = Vacancy('123456', 'Разраб', 'http:/1.ru', '1000', '100000', 'Оч хорошая, не напряжная такая, сойдет',
              #'A&B', 'hh.ru')
#vac2 = Vacancy('123458', 'Разраб2', 'http:/1.ru', '1000', '10000', 'Оч хорошая, не напряжная такая, сойдет',
              #'A&B', 'hh.ru')

#print(Vacancy.get_json_from_vacancy())
#Vacancy.delete_vacancy('123456')
#print(Vacancy.get_json_from_vacancy())
# print(vac.__class__.__dict__)

# print(vac)
# print(repr(vac))
