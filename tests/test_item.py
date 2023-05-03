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
