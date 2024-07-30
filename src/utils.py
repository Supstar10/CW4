from src.filemanager import GetFile
from src.hh_api import HH
from src.vacancy import Vacancy


def sorted_by_salary(vacancy):
    """Функция сортировки вакансий"""
    return sorted(vacancy, reverse=True)


def filter_by_keyword(vacancy):
    keyword = input("Введите ключевое слово для фильтрации:")
    for i in vacancy:
        if keyword in i.requirement:
            print(i)

def user_interaction():
    # Функция для взаимодействия с пользователем
    keyword = input("Введите ключевое слово для поиска вакансии: ")

    per_page = int(input("Введите количество вакансий для вывода: "))

    hh = HH()

    vacancy = hh.load_vacancies(keyword, per_page)

    vacancies = [Vacancy.from_hh_dict(vacancy) for vacancy in vacancy]
    sorted_vacancies = sorted_by_salary(vacancies)
    print("Вакансии по запросу\n")
    for i in sorted_vacancies:
        print(i)

    filter_by_keyword(sorted_vacancies)
    get_file = GetFile("data/vacancies.json")
    vacancies = [vacancy.to_dict() for vacancy in vacancies]
    get_file.add_data(vacancies)
    print("Данные записаны в файл")
    user_input = input("Введите да, если хотите удалить данные\n").lower()

    if user_input == "да":
        get_file.del_data()
    else:
        return
