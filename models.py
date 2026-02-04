
class Loses:
    def __init__(self, warriors: int = 0, hunters: int = 0, wizards: int = 0):
        self.nb_warriors = warriors
        self.nb_hunters = hunters
        self.nb_wizards = wizards


class Game:
    history_file = 'game_data.txt'

    def __init__(self):
        self.__game_status = 'not_started'

    def config(self):
        # Logique de configuration ici
        pass

    def status(self):
        print(f'Statut actuel : {self.__game_status}')

