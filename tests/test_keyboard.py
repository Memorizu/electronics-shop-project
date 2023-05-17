
class TestKeyboard:

    def test_init(self, keyboard_obj):
        assert keyboard_obj.name == 'Dark Project KD87A'

    def test_language(self, keyboard_obj):
        assert keyboard_obj.language == 'EN'

    def test_str(self, keyboard_obj):
        assert str(keyboard_obj) == 'Dark Project KD87A'

    def test_change_lang(self, keyboard_obj):
        keyboard_obj.change_lang()
        assert keyboard_obj.language == 'RU'
        keyboard_obj.change_lang()
        assert keyboard_obj.language == 'EN'

