
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


    def buy(self, unit_type):
        prices = {'warrior': 10, 'hunter': 12, 'wizard': 15}
        if unit_type in prices:
            # Sauvegarde simulée dans history_file
            with open(self.history_file, 'a') as f:
                f.write(f'Achat: {unit_type}
')
            return True
        return False


    def move(self):
        # Simule le chargement et le calcul de mouvement
        print('Personnage en mouvement...')
        with open(self.history_file, 'a') as f:
            f.write('Action: Move
')
        self.status()


    def fight(self):
        # Simule un combat
        print('Combat en cours...')
        with open(self.history_file, 'a') as f:
            f.write('Action: Fight
')
        self.status()

