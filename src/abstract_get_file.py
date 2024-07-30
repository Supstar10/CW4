from abc import ABC, abstractmethod


class GetFileABC(ABC):
    """Абстрактный класс для записи в файл"""

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def add_data(self, file_name):
        pass

    @abstractmethod
    def del_data(self):
        pass
