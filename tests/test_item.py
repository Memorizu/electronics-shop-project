
import pytest

from exceptions import TooLongName, WrongObj
from src.item import Item


class TestItem:

    def test_all(self, item_obj1, item_obj2):
        assert Item.all == [item_obj1, item_obj2]
        assert len(Item.all) == 2

    def test_calculate_total_price(self, item_obj1, item_obj2):
        assert item_obj1.calculate_total_price() == 500
        assert item_obj2.calculate_total_price() == 2500

    def test_apply_discount(self, item_obj3):
        item_obj3.apply_discount()
        assert item_obj3.price == 80
        assert item_obj3.calculate_total_price() == 400

    def test_read_scv_file(self):
        data = Item.read_csv_file('items.csv')
        assert len(data) == 5
        assert data[0]['name'] == 'Смартфон'

    def test_read_scv_error(self):
        with pytest.raises(FileNotFoundError):
            Item.read_csv_file('src/items.csv')

    def test_name(self, item_obj1):
        assert item_obj1.name == 'test'

    def test_name_setter(self, item_obj1):
        item_obj1.name = 'Аппарат'
        assert item_obj1.name == 'Аппарат'

    def test_name_exception(self, item_obj1):
        with pytest.raises(TooLongName):
            item_obj1.name = 'СуперАппарат'

    def test_string_to_number(self):
        assert Item.string_to_number('4') == 4
        assert Item.string_to_number('5.5') == 5

    def test_instantiate_from_scv(self):
        Item.instantiate_from_csv()
        assert len(Item.all) == 5
        assert Item.all[0].name == 'Смартфон'

    def test_repr(self, item_obj1):
        assert item_obj1.__repr__() == "Item('test', 100, 5)"

    def test_str(self, item_obj1):
        assert item_obj1.__str__() == 'test'

    def test_add(self, item_obj1, item_obj2, phone_obj, unknown_obj):
        assert item_obj1 + item_obj2 == 15
        assert item_obj1 + phone_obj == 10
        with pytest.raises(WrongObj):
            item_obj1 + unknown_obj()

