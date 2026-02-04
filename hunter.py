import random


class Hunter:
    def __init__(self):
        self.degat = random.choice(range(1, 3))  # 1 ou 2
        self.chance = 10
        self.fuite = 20
        self.prix = 25
        self.type_unite = "hunter"
