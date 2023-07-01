# 3. Создать класс для работы с вакансиями, определить атрибуты:
#       - название вакансии
#       - ссылка на вакансию
#       - зарплата
#       - краткое описание/требования

class Vacancy:

    __slots__ = ('__v_id', '__name', '__link', '__salary_from', '__salary_to', '__description',
                 '__company', '__api')

    def __init__(self, v_id, name, link, salary_from, salary_to, description, company, api):
        self.__v_id = v_id
        self.__name = name
        self.__link = link
        self.__salary_from = salary_from
        self.__salary_to = salary_to
        self.__description = description
        self.__company = company
        self.__api = api

    def __repr__(self):
        """
        Переопределение метода repr
        Вывод полной информации о вакансии
        :return: строка с данными о вакансии
        """
        desc = self.__description
        if len(self.__description) > 25:
            desc = self.__description[:25] + '...'

        return f"id: {self.__v_id} name: {self.__name}, link: {self.__link}, " \
               f"salary: {self.__salary_from} - {self.__salary_to}, " \
               f"description: {desc}, company - {self.__company}"

    def __str__(self):
        pay = str(self.__salary_from) + '-' + str(self.__salary_to)
        return f'Вакансия: {self.__name} с З/П: {pay} в организацию {self.__company}'

    def __eq__(self, other) -> bool:

        """
               =
               :param other:
               :return:
               """
        if self.__salary_from == other.__salary_from:
            return True
        else:
            return False

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
        

vac = Vacancy('123456', 'Разраб', 'http:/1.ru', '1000', '100000', 'Оч хорошая, не напряжная такая, сойдет',
              'A&B', 'hh.ru')
vac2 = Vacancy('123458', 'Разраб2', 'http:/1.ru', '1000', '10000', 'Оч хорошая, не напряжная такая, сойдет',
               'A&B', 'hh.ru')

#print(vac2 == vac)

# print(vac)
#print(repr(vac))
