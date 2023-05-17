
class KeyboardMixin:

    def __init__(self) -> None:
        self.__language = 'EN'

    def __str__(self) -> str:
        return self.__language

    @property
    def language(self) -> str:
        return self.__language

    def change_lang(self) -> 'KeyboardMixin':
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'
        return self
