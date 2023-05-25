from exceptions import TooLongName, WrongObj, InstantiateCSVError
from csv import DictReader
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__()
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        raise WrongObj('Неверный объект для сложения количества')

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        """
        Геттер для параметра name
        """
        return self.__name

    @name.setter
    def name(self, new_name: str):
        """
        Сеттер для параметра name
        Вызывает ошибку если передан name свыше 9 символов
        """
        if len(new_name) <= 10:
            self.__name = new_name
        else:
            raise TooLongName('Exception: Длина наименования товара превышает 10 символов.')

    @staticmethod
    def read_csv_file(path: str) -> [list, str]:
        """
        Читает данные из csv файла
        Возвращает данные в формате list
        """

        list_of_items = []
        with open(os.path.join(path), encoding='windows-1251') as f:
            file = DictReader(f)
            for item in file:
                if len(item) < 3:
                    raise InstantiateCSVError
                list_of_items.append(item)
        return list_of_items

    @staticmethod
    def string_to_number(string: str) -> [int, float]:
        """
        Статический метод
        Переводит строку в int или float и округляет в меньшую сторону.
        """
        if '.' in string:
            return float(string) // 1
        else:
            return int(string)

    @classmethod
    def instantiate_from_csv(cls, path) -> [None, str]:
        """
        Заполняет параметр all у класса данными из csv файла
        """

        cls.all = []
        try:
            data = cls.read_csv_file(path)
            for item in data:
                cls(
                    item['name'],
                    cls.string_to_number(item['price']),
                    cls.string_to_number(item['quantity'])
                )
        except InstantiateCSVError:
            return 'Файл повережден'
        except FileNotFoundError:
            return 'Файл не найден'


# print(Item.instantiate_from_csv('../test.csv'))