import random
import json

# --- #11 : TeamIterator ---
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

# --- #10 : Team (Abstraite) ---
class Team:
    def __init__(self, members):
        self._members = members  # Protégé

    def __len__(self):
        return len(self._members)

    def __getitem__(self, index):
        return self._members[index]

    def __iter__(self):
        return TeamIterator(self._members)

# --- #12 : EnemyTeam ---
class EnemyTeam(Team):
    def __init__(self, unit_type, members):
        super().__init__(members)
        self.__unit = unit_type
        self.__damage = sum(getattr(u, 'degat', 0) for u in members)
        self.__loot = random.randint(10, 30)

    def get_damage(self): return self.__damage
    def get_loot(self): return self.__loot
    def get_unit_type(self): return self.__unit

# --- #13 : PlayerTeam ---
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
