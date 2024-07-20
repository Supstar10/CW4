import json

from abstract_get_file import GetFileABC


class GetFile(GetFileABC):

    def __init__(self, file_name):
        """Конструктор класса"""
        super().__init__(file_name)

    def get_data(self, file_name):
        """Читает данные из JSON файла и возвращает их."""

        try:
            return json.load(open(self.file_name))
        except FileNotFoundError:
            return []

    def add_data(self, file_name, new_data):
        """Добавляет новые данные в JSON файл."""
        data = self.get_data(file_name)
        data.extend(new_data)

        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def del_data(self, file_name):
        """Удаляет данные из файла"""
        with open(file_name, 'w', encoding='utf-8') as file:
            json.dump([], file, ensure_ascii=False, indent=4)