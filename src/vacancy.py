class Vacancy:
    """
    Класс для работы с вакансиями
    """

    __slots__ = ("name", "area_name", "salary_from", "salary_to", "alternate_url", "requirement", "responsibility")

    def __init__(self, name, area_name, salary_from, salary_to, alternate_url, requirement, responsibility):
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
        return (
            f"Название вакансии: {self.name}"
            f"Место работы: {self.area_name}"
            f"ЗП от: {self.salary_from}"
            f"ЗП до: {self.salary_to}"
            f"Ссылка на вакансию: {self.alternate_url}"
            f"Краткое описание: {self.requirement}"
            f"Требования: {self.responsibility}"
                )

    @classmethod
    def from_hh_dict(cls, data):

        salary = data.get("salary")

        return cls(
            data["name"],
            data["area"]["name"],
            salary.get("from") if salary.get("from") else 0,
            salary.get("to") if salary.get("to") else 0,
            data["snippet"]["requirement"],
            data["snippet"]["responsibility"],
            data["alternate_url"]
        )


