import Team

class PlayerTeam(Team):
    def __init__(self, members, nb_warriors, nb_hunters, nb_wizards, damage, loot, flee):
        super().__init__(members)
        self.__nb_warriors = nb_warriors
        self.__nb_hunters = nb_hunters
        self.__nb_wizards = nb_wizards
        self.__damage = damage
        self.__loot = loot
        self.__flee = flee
    
    def get_damage(self):
        return self.__damage
    
    def get_loot(self):
        return self.__loot
    
    def get_flee(self):
        return self.__flee
    
    def get_nb_warriors(self):
        return self.__nb_warriors
    
    def get_nb_hunters(self):
        return self.__nb_hunters
    
    def get_nb_wizards(self):
        return self.__nb_wizards
    
    def __repr__(self):
        return (f"PlayerTeam(Warriors={self.__nb_warriors}, Hunters={self.__nb_hunters}, "
                f"Wizards={self.__nb_wizards}, Damage={self.__damage}, Loot={self.__loot}, Flee={self.__flee})")
