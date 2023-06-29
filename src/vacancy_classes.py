# 3. Создать класс для работы с вакансиями, определить атрибуты:
#       - название вакансии
#       - ссылка на вакансию
#       - зарплата
#       - краткое описание/требования

class Vacancy:

    def __init__(self, vac_name, vac_reference='', vac_salary=0.0, vac_resp=''):
        self.vac_name = vac_name
        self.vac_reference = vac_reference
        self.vac_salary = vac_salary
        self.vac_resp = vac_resp

    