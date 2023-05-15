import pytest

from src.phone import Phone


class TestPhone:

    def test_repr(self, phone_obj):
        assert repr(phone_obj) == "Phone('iPhone 14', 120000, 5, 2)"


    def test_init(self):
        with pytest.raises(ValueError):
            Phone("iPhone 14", 120_000, 5, 0)
