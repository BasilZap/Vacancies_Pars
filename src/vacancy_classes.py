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
        #if self.salary_from in (0, '0'):
            #salary_from_show = 'не указана'
        #else:
            #salary_from_show = self.salary_to
        #if int(self.salary_to) in (0, '0'):
            #salary_to_show = 'не указана'
        #else:
            #salary_to_show = self.salary_to
        desc = self.description
        if len(self.description) > 25:
            desc = self.description[:25] + '...'

        return f"id: {self.v_id}, name: {self.name}, link: {self.link}, " \
               f"salary: {self.salary_from} - {self.salary_to}, " \
               f"description: {desc}, company - {self.company}, api - {self.api}"

    def __str__(self):
        pay = str(self.salary_from) + '-' + str(self.salary_to)
        return f'Вакансия: {self.name} с З/П: {pay} в организацию {self.company}'

    def get_json_from_vacancy(self):
        rec = {'id': self.v_id, 'name': self.name, 'url': self.link, 'salary_from': self.salary_from,
               'salary_to': self.salary_to, 'description': self.description, 'company': self.company, 'api': self.api}
        return rec

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
        

# vac = Vacancy('123456', 'Разраб', 'http:/1.ru', '1000', '100000', 'Оч хорошая, не напряжная такая, сойдет',
            # 'A&B', 'hh.ru')
# v ac2 = Vacancy('123458', 'Разраб2', 'http:/1.ru', '1000', '10000', 'Оч хорошая, не напряжная такая, сойдет',
            # 'A&B', 'hh.ru')

# print(vac2.get_json_from_vacancy())
# print(vac.__class__.__dict__)

# print(vac)
# print(repr(vac))
