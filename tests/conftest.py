import pytest
from src.item import Item


@pytest.fixture
def item_obj1():
    item = Item('test', 100, 5)
    return item


@pytest.fixture
def item_obj2():
    return Item('test', 250, 10)


@pytest.fixture
def item_obj3():
    item = Item('test', 100, 5)
    Item.pay_rate = 0.8
    return item
