import pytest


from src.item import Item

@pytest.fixture
def item():
    return Item("Смартфон", 10000, 20)


def item():
    item = Item('Телефон', 10000, 5)

def item():
    item1 = Item("Смартфон", 10000, 20)

