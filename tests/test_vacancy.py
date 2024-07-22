import pytest

from src.vacancy import Vacancy


class TestVacancy:

    @pytest.fixture
    def vacancy1(self):
        """Создание объекта Vacancy для тестов"""
        return Vacancy("Программист", "Москва", 100000, 150000, "http://example.com", "Знание Python",
                       "Разработка приложений")

    @pytest.fixture
    def vacancy2(self):
        """Создание другого объекта Vacancy для тестов"""
        return Vacancy("Тестировщик", "Санкт-Петербург", 80000, 120000, "http://example.com/2", "Знание тестирования",
                       "Тестирование ПО")

    def test_str(self, vacancy1):
        """Тестирование метода str"""
        expected_output = (
            "Название вакансии: Программист\n"
            "Место работы: Москва\n"
            "ЗП от: 100000\n"
            "ЗП до: 150000\n"
            "Ссылка на вакансию: http://example.com\n"
            "Краткое описание: Знание Python\n"
            "Требования: Разработка приложений\n"
        )
        assert vacancy1.__str__() == expected_output, "Вывод должен совпадать с ожидаемым"

    def test_from_hh_dict(self):
        """Тестирование метода from_hh_dict"""
        data = {
            "name": "Разработчик",
            "area": {"name": "Казань"},
            "salary": {"from": 90000, "to": 130000},
            "alternate_url": "http://example.com/3",
            "snippet": {
                "responsibility": "Создание приложений",
                "requirement": "Знание Go"
            }
        }
        vacancy = Vacancy.from_hh_dict(data)
        assert vacancy.name == "Разработчик"
        assert vacancy.area_name == "Казань"
        assert vacancy.salary_from == 90000
        assert vacancy.salary_to == 130000

    def test_to_dict(self, vacancy1):
        """Тестирование метода to_dict"""
        expected_dict = {
            "name": "Программист",
            "area_name": "Москва",
            "salary_from": 100000,
            "salary_to": 150000,
            "alternate_url": "http://example.com",
            "requirement": "Знание Python",
            "responsibility": "Разработка приложений"
        }
        assert vacancy1.to_dict() == expected_dict, "Метод to_dict должен возвращать правильный словарь"
