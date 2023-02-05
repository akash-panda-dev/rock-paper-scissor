from typing import Any
from abc import ABC, abstractmethod


class GameStrategy(ABC):
    @abstractmethod
    def play(self, hand: Any) -> str:
        """Return a string based on which hand won."""
        pass
