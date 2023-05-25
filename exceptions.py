
class TooLongName(Exception):
    def __init__(self, message=None):
        self.message = message


class WrongObj(Exception):
    def __init__(self, message=None):
        self.message = message


class InstantiateCSVError(Exception):
    def __init__(self, message=None):
        self.message = message
