class Humain:
    def __init__(self):
        self.name = 'name'
        self.age = 21

    def _getage(self):
        return self.age

    def _setage(self, age):
        self.age = age

    def _delage(self):
        del self.age

    age = property(_getage, _setage, _delage, "manage age of humain")
