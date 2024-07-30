import requests

from src.abstract_get_vacancies_api import GetVacanciesAPI


class HH(GetVacanciesAPI):
    """
    Класс для работы с API HeadHunter
    Класс GetVacanciesAPI является родительским классом
    """

    def __init__(self):
        """конструктор класса"""
        self.__url = 'https://api.hh.ru/vacancies'
        self._headers = {'User-Agent': 'HH-User-Agent'}
        self._params = {"only_with_salary": True}

    def load_vacancies(self, keyword, per_page):
        """загрузка вакансий"""
        self._params['text'] = keyword
        self._params['per_page'] = per_page
        response = requests.get(self.__url, headers=self._headers, params=self._params)
        vacancies = response.json()['items']
        return vacancies
