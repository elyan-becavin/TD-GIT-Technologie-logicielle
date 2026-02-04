import random


class Warrior:
    def __init__(self):
        self.degat = random.choice(range(3, 6))  # 3, 4 ou 5
        self.chance = 5
        self.fuite = 3
        self.prix = 10
        self.type_unite = "warrior"
