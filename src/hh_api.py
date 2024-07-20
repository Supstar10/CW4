import requests

from src.abstract_get_vacancies_api import GetVacanciesAPI


class HH(GetVacanciesAPI):
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом, который вам необходимо реализовать
    """

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 20, "only_with_salary": True}
        self.vacancies = []
        #super().__init__(file_worker)

    def load_vacancies(self, keyword):
        self.params['text'] = keyword
        #return requests.get(self.url, headers=self.headers, params=self.params)
        while self.params.get('page') != 2:
           response = requests.get(self.url, headers=self.headers, params=self.params)
           vacancies = response.json()['items']
           self.vacancies.extend(vacancies)
           self.params['page'] += 1
        return self.vacancies


hh = HH()
response = hh.load_vacancies("Разработчик")
print(response)
print(len(response))
#get_url = 'https://api.hh.ru/vacancies'
#response = requests.get(get_url)
#print(response)