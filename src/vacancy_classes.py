# 3. Создать класс для работы с вакансиями, определить атрибуты:
#       - название вакансии
#       - ссылка на вакансию
#       - зарплата
#       - краткое описание/требования

class Vacancy:

    __slots__ = ('__name', '__link', '__salary_from', '__salary_to', '__description', '__responsible', '__company')

    def __init__(self, name, link, salary_from, salary_to, description, responsible, company):
        self.__name = name
        self.__link = link
        self.__salary_from = salary_from
        self.__salary_to = salary_to
        self.__description = description
        self.__responsible = responsible
        self.__company = company

    def __repr__(self):
        """
        Переопределение метода repr
        Вывод полной информации о вакансии
        :return: строка с данными о вакансии
        """
        desc = self.__description
        if len(self.__description) > 25:
            desc = self.__description[:25] + '...'
        resp = self.__responsible
        if len(self.__responsible) > 25:
            resp = self.__responsible[:25] + '...'
        return f"name: {self.__name}, link: {self.__link}, " \
               f"salary: {self.__salary_from} - {self.__salary_to}, " \
               f"description: {desc}, " \
               f"responsibility: {resp}, company - {self.__company}"

    def __str__(self):
        pay = str(self.__salary_from) + '-' + str(self.__salary_to)
        return f'Вакансия: {self.__name} с З/П: {pay} в организацию {self.__company}'

    def __lt__(self, other):
        """
        <
        :param other:
        :return:
        """
        if self.__salary_from < other.__salary_from:
            return True
        else:
            return False

    def __le__(self, other):
        """
        <=
        :param other:
        :return:
        """
        if self.__salary_from <= other.__salary_from:
            return True
        else:
            return False

    def __gt__(self, other):
        """
        >
        :param other:
        :return:
        """
        if self.__salary_from > other.__salary_from:
            return True
        else:
            return False

    def __ge__(self, other):
        """
        >=
        :param other:
        :return:
        """
        if self.__salary_from >= other.__salary_from:
            return True
        else:
            return False
        

vac = Vacancy('Разраб', 'http:/1.ru', '1000', '100000', 'Оч хорошая, не напряжная такая, сойдет',
              'Спать, главное при этом как можно больше работать', 'A&B')

# print(vac)
print(repr(vac))
