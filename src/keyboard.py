from src.item import Item
from src.keyboardmixin import KeyboardMixin


class KeyBoard(Item, KeyboardMixin):

    __language = 'EN'

    def __str__(self):
        return self.name



