import pytest
from src.item import Item
from src.phone import Phone
from src.keyboard import KeyBoard


@pytest.fixture
def item_obj1():
    item = Item('test', 100, 5)
    return item


@pytest.fixture
def unknown_obj():
    return int


@pytest.fixture
def item_obj2():
    return Item('test', 250, 10)


@pytest.fixture
def item_obj3():
    item = Item('test', 100, 5)
    Item.pay_rate = 0.8
    return item


@pytest.fixture
def phone_obj():
    return Phone("iPhone 14", 120_000, 5, 2)


@pytest.fixture
def phone_obj_negative():
    return Phone("iPhone 14", 120_000, 5, 0)

@pytest.fixture
def keyboard_obj():
    kb = KeyBoard('Dark Project KD87A', 9600, 5)
    return kb
