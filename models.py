
class Wizard:
    def __init__(self):
        self.degat = random.choice([2, 3, 4])
        self.chance = 20
        self.fuite = 10
        self.prix = 15
        self.type_unite = 'wizard'


class Zombie:
    def __init__(self):
        self.degat = random.choice([1, 2])
        self.loot = random.choice([0.5, 1])

