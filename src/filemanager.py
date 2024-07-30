import json

from src.abstract_get_file import GetFileABC


class GetFile(GetFileABC):

    def __init__(self, file_name):
        """Конструктор класса"""
        self.__file_name = file_name

    def get_data(self):
        """Читает данные из JSON файла и возвращает их."""
        try:
            with open(self.__file_name, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def add_data(self, new_data):
        """Добавляет новые данные в JSON файл."""
        data = self.get_data()
        data.extend(new_data)

        with open(self.__file_name, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def del_data(self):
        """Удаляет данные из файла"""
        with open(self.__file_name, 'w', encoding='utf-8') as file:
            json.dump([], file, ensure_ascii=False, indent=4)
