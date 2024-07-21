# Функция для взаимодействия с пользователем
from src.filemanager import GetFile
from src.hh_api import HH
from src.vacancy import Vacancy


def user_interaction():
    keyword = input("Введите поисковый запрос: ")

    per_page = int(input("Введите количество вакансий для вывода: "))

    hh = HH()

    vacancy = hh.load_vacancies(keyword, per_page)
    vacancies = [Vacancy.from_hh_dict(vacancy) for vacancy in vacancy]
    sorted_vacancies = sorted(vacancies, reverse=True)
    print("Вакансии по запросу\n")
    for i in sorted(sorted_vacancies, reverse=True):
        print(i)

    get_file = GetFile("data/vacancies.json")
    vacancies = [vacancy.to_dict() for vacancy in vacancies]
    get_file.add_data(vacancies)
    get_file.get_data()
    print("Данные записаны в файл")

    user_input = input("Введите да, если хотите удалить данные\n").lower()
    if user_input == "да":
        get_file.del_data()
    else:
        return


if __name__ == "__main__":
    user_interaction()
