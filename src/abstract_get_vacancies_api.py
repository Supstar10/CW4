from abc import ABC, abstractmethod


class GetVacanciesAPI(ABC):
    @abstractmethod
    def load_vacancies(self, keyword):
        pass
