import requests

from src.abstract_get_vacancies_api import GetVacanciesAPI


class HH(GetVacanciesAPI):
    """
    Класс для работы с API HeadHunter
    Класс GetVacanciesAPI является родительским классом
    """

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'per_page': "", "only_with_salary": True}
        self.vacancies = []

    def load_vacancies(self, keyword, per_page):
        self.params['text'] = keyword
        self.params['per_page'] = per_page
        response = requests.get(self.url, headers=self.headers, params=self.params)
        vacancies = response.json()['items']
        return vacancies
