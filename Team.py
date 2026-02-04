from abc import ABC, abstractmethod

class Team(ABC):
    def __init__(self, members):
        self._members = members

    def __len__(self):
        return len(self._members)
    
    def __getitem__(self, index):
        return self._members[index]

    # Optionnel, pour itération
    def __iter__(self):
        return TeamIterator(self)

class TeamIterator:
    def __init__(self, team):
        self.__team = team
        self.__index = 0

    def __next__(self):
        if self.__index < len(self.__team):
            result = self.__team[self.__index]
            self.__index += 1
            return result
        else:
            raise StopIteration()
