from abc import ABC
from typing import Iterable, List, Any, Iterator


class Team(ABC):
    def __init__(self, members: Iterable[Any]):
        self._members: List[Any] = list(members)

    def __len__(self) -> int:
        return len(self._members)

    def __getitem__(self, index: int) -> Any:
        return self._members[index]

    # Optionnel : itération (for x in team)
    def __iter__(self) -> Iterator[Any]:
        return iter(self._members)

    # Si plus tard vous faites TeamIterator (optionnel #8), vous remplacerez __iter__ par :
    # def __iter__(self) -> "TeamIterator":
    #     return TeamIterator(self._members)
