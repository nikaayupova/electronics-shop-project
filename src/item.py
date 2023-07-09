from csv import DictReader

from settings import PATH_CSV_ITEMS
class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    items_csv_path = PATH_CSV_ITEMS

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self):
        return self.__name


    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            self.__name = name[:10]


    @classmethod
    def instantiate_from_csv(cls):
        cls.all = []
        with open(cls.items_csv_path, 'r', encoding='utf8') as csv:
            data = DictReader(csv)
            for item in data:
                cls(
                    name=item['name'],
                    price=cls.string_to_number(item['price']),
                    quantity=cls.string_to_number(item['quantity'])
                )


    @staticmethod
    def string_to_number(decimal_string):
        return int(float(decimal_string))


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
        return self.pay_rate

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return f"{__class__.__name__}('{str(self.__name)}', {str(self.price)}, {str(self.quantity)})"
