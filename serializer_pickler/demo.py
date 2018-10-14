class Player:
    def __init__(self):
        self.name = 'lol'
        self.age = 52

p1 = Player()

"""
write data
"""
with open('file.data', 'wb') as file:
    record = pickler.Pickler(file)
    record.dump(p1)

"""
load data
"""
with open('file.data', 'rb') as file:
    get_reccord = pickler.Unpickler(file)
    player = get_reccord.load()