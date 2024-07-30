class Vacancy:
    """
    Класс для работы с вакансиями
    """

    __slots__ = ("name", "area_name", "salary_from", "salary_to", "alternate_url", "requirement", "responsibility")

    def __init__(self, name, area_name, salary_from, salary_to, alternate_url, requirement, responsibility):
        """конструктор класса"""
        self.name: str = name
        self.area_name: str = area_name
        self.salary_from: int = salary_from
        self.salary_to: int = salary_to
        self.alternate_url: str = alternate_url
        self.requirement: str = requirement
        self.responsibility: str = responsibility

    def __lt__(self, other) -> bool:
        """
        Получает булевый тип
        :param other:
        :return: либо true либо false
        """
        if isinstance(other, Vacancy):
            return self.salary_from < other.salary_from

    def __str__(self):
        """функция вывода"""
        return (
            f"Название вакансии: {self.name}\n"
            f"Место работы: {self.area_name}\n"
            f"ЗП от: {self.salary_from}\n"
            f"ЗП до: {self.salary_to}\n"
            f"Ссылка на вакансию: {self.alternate_url}\n"
            f"Краткое описание: {self.requirement}\n"
            f"Требования: {self.responsibility}\n"
        )

    @classmethod
    def from_hh_dict(cls, data):
        """создание экземпляра класса"""
        salary = data.get("salary")

        return cls(
            data["name"],
            data["area"]["name"],
            salary.get("from") if salary.get("from") else 0,
            salary.get("to") if salary.get("to") else 0,
            data["alternate_url"],
            data["snippet"]["responsibility"],
            data["snippet"]["requirement"]
        )

    def to_dict(self):
        """получения словаря с вакансиями"""
        return {"name": self.name,
                "area_name": self.area_name,
                "salary_from": self.salary_from,
                "salary_to": self.salary_to,
                "alternate_url": self.alternate_url,
                "requirement": self.requirement,
                "responsibility": self.responsibility
                }
