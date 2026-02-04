import random
import json

class TeamIterator:
    def __init__(self, team_members):
        self.__team = team_members
        self.__index = 0
    def __next__(self):
        if self.__index < len(self.__team):
            member = self.__team[self.__index]
            self.__index += 1
            return member
        raise StopIteration

class Team:
    def __init__(self, members):
        self._members = members
    def __len__(self): return len(self._members)
    def __getitem__(self, index): return self._members[index]
    def __iter__(self): return TeamIterator(self._members)

class EnemyTeam(Team):
    def __init__(self, unit_type, members):
        super().__init__(members)
        self.__unit = unit_type
        self.__damage = sum(getattr(u, 'degat', 0) for u in members)
        self.__loot = random.randint(10, 30)
    def get_damage(self): return self.__damage
    def get_loot(self): return self.__loot
    def get_unit_type(self): return self.__unit

class PlayerTeam(Team):
    def __init__(self, warriors=0, hunters=0, wizards=0):
        members = (['W'] * warriors) + (['H'] * hunters) + (['Z'] * wizards)
        super().__init__(members)
        self.__nb_warriors = warriors
        self.__nb_hunters = hunters
        self.__nb_wizards = wizards
        self.__damage = (warriors * 5) + (hunters * 4) + (wizards * 3)
        self.__flee = (warriors * 1) + (hunters * 3) + (wizards * 5)
        self.__luck = (hunters * 2)
    def get_damage(self): return self.__damage
    def get_flee_value(self): return self.__flee
    def get_luck(self): return self.__luck
    def get_counts(self):
        return {"warriors": self.__nb_warriors, "hunters": self.__nb_hunters, "wizards": self.__nb_wizards}
    def __repr__(self):
        return f"PlayerTeam(W:{self.__nb_warriors}, H:{self.__nb_hunters}, Z:{self.__nb_wizards})"

class Game:
    history_file = 'game_data.json'

    def save_game(self, player_name, context, loot, team_counts):
        data = {'player_name': player_name, 'context': context, 'loot': loot, 'team': team_counts}
        with open(self.history_file, 'w') as f:
            json.dump(data, f, indent=4)

    def load_game(self):
        try:
            with open(self.history_file, 'r') as f: return json.load(f)
        except FileNotFoundError: return None

    def start(self):
        data = self.load_game()
        name = data['player_name'] if data else "Joueur"
        self.save_game(name, 'mouvement', 40, {'warriors': 0, 'hunters': 0, 'wizards': 0})
        print("Partie réinitialisée !")

    def status(self):
        data = self.load_game()
        if not data: return print("Aucune partie. Tapez start()")
        team = PlayerTeam(data['team']['warriors'], data['team']['hunters'], data['team']['wizards'])
        print(f"\n--- {data['player_name']} | Butin: {data['loot']} ---")
        print(f"Équipe: {team} | Contexte: {data['context']}")

    def move(self):
        data = self.load_game()
        if not data or data['context'] != 'mouvement': return
        print('Déplacement en cours...')
        r = random.random()
        if r < 0.2:
            print("Butin trouvé !"); data['loot'] += 20
        elif r < 0.4:
            print("COMBAT !"); data['context'] = 'combat'
        else:
            print("Lieu sûr.")
        self.save_game(data['player_name'], data['context'], data['loot'], data['team'])
