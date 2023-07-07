from src.api_classes import HeadHunterAPI, SuperJobAPI
from src.json_exchange_class import JSONSaver
from src.vacancy_classes import Vacancy

# 6. Создать функцию для взаимодействия с пользователем
hh_api = HeadHunterAPI()
sj_api = SuperJobAPI()
j_saver = JSONSaver()
vacancy = Vacancy


def user_interaction():

    while True:
        print(f'==================================================================================')
        print(f'Добро пожаловать в программу работы с вакансиями с сайтов HeadHunter и SuperJob!!!')
        print(f'Укажите, с каким сайтом будем работать:')
        print(f'"1" - Работа с HeadHunter.ru')
        print(f'"2" - Работа с SuperJob.ru')
        print(f'Enter - HeadHunter.ru + SuperJob.ru')
        answer = input('Введите Exit для выхода\n')
        if answer.lower() not in ("1", "2", "", "exit"):
            print('Некорректный ввод, проверьте раскладку клавиатуры и введите один из предлагаемых вариантов\n')
        else:
            if answer == '1':
                print('Выбрана работа с сайтом HeadHunter.ru')
                work_with_hh()
                second_menu()
            elif answer == '2':
                print('Выбрана работа с сайтом SuperJob.ru')
                work_with_sj()
                second_menu()
            elif answer == '':
                print('Выбрана работа с сайтами HeadHunter.ru и SuperJob.ru')
                work_with_both_platforms()
                second_menu()
            else:
                exit()


def work_with_hh():
    profession = input('Ведите название вакансии:\n')
    area = input('Ведите город в котором нужно искать или нажмите Enter - поиск по России:\n')
    hh_api.find_area_id(area)
    hh_api.get_api_data(profession)
    data = hh_api.get_api_vacancy_json_list()
    j_saver.save_raw_to_json(data)
    vacancy.get_vacancies(j_saver.vacancies)


def work_with_sj():
    profession = input('Ведите название вакансии:\n')
    area = input('Ведите город в котором нужно искать или нажмите Enter - поиск по России:\n')
    sj_api.area = area
    sj_api.get_api_data(profession)
    data = sj_api.get_api_vacancy_json_list()
    j_saver.save_raw_to_json(data)
    vacancy.get_vacancies(j_saver.vacancies)


def work_with_both_platforms():
    profession = input('Ведите название вакансии:\n')
    area = input('Ведите город в котором нужно искать или нажмите Enter - поиск по России:\n')
    hh_api.find_area_id(area)
    hh_api.get_api_data(profession)
    sj_api.area = area
    sj_api.get_api_data(profession)
    hh_data = hh_api.get_api_vacancy_json_list()
    sj_data = sj_api.get_api_vacancy_json_list()
    data = vacancy.vacancy_data_splitter(hh_data, sj_data)
    j_saver.save_raw_to_json(data)
    vacancy.get_vacancies(j_saver.vacancies)


def second_menu():
    while True:
        print("=======================================================================================")
        print(f"Работа с вакансиями, Ваши действия:")
        print(f"1 - Показать несколько вакансий или все вакансии")
        print(f"2 - Сортировать вакансии по минимальной зарплате")
        print(f"3 - Добавить вакансию")
        print(f"4 - Удалить вакансию")
        print(f"5 - Сохранить вакансии в файл")
        print(f"6 - Вернуться на первый экран")
        answer = input('Введите Exit для выхода\n')
        if answer.lower() in ("1", "2", "3", "4", "5", "6", "exit"):
            if answer == "1":
                vac_number = input("Введите количество вакансий для вывода, или нажмите Enter - показать все вакансии\n")
                if vac_number.isdigit():
                    vacancy.show_n_vacancies(int(vac_number))
                elif vac_number == '':
                    vacancy.show_n_vacancies()
                else:
                    print('Некорректный ввод, повторите попытку\n')
            elif answer == "2":
                vacancies = vacancy.get_json_from_vacancy()
                sorted_vacancies = vacancy.get_vacancy_by_salary(vacancies)
                vacancy.get_vacancies(sorted_vacancies)
                vacancy.show_n_vacancies()

            elif answer == "3":
                v_id = input("Введите ID вакансии\n")
                name = input("Введите название вакансии\n")
                link = input("Введите ссылку на вакансию\n")
                salary_from = input("Введите минимальную з/п для вакансии\n")
                salary_to = input("Введите максимальную з/п для вакансии\n")
                description = input("Введите описание вакансии\n")
                company = input("Введите название компании\n")
                vacancy.add_vacancy(v_id, name, link, salary_from, salary_to, description, company)
                print(f'Вакансия {repr(vacancy.all[-1])} успешно добавлена')
            elif answer == "4":
                vacancy_to_del = input('Введите ID вакансии для удаления:\n')
                vacancy.delete_vacancy(vacancy_to_del)
            elif answer == "5":
                j_saver.save_raw_to_json(vacancy.get_json_from_vacancy())
            elif answer == "6":
                user_interaction()
            else:
                exit()
        else:
            print('Некорректный ввод, проверьте раскладку клавиатуры и введите один из предлагаемых вариантов\n')


user_interaction()
