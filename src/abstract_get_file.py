from abc import ABC, abstractmethod


class GetFileABC(ABC):
    """Абстрактный класс для записи в файл"""

    def __init__(self, file_name):
        self.file_name = file_name

    @abstractmethod
    def get_data(self, file_name):
        pass

    @abstractmethod
    def add_data(self, file_name):
        pass

    @abstractmethod
    def del_data(self, file_name):
        pass
