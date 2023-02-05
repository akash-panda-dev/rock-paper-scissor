from game_strategy.game_strategy_interface import GameStrategy
from abc import ABC, abstractmethod


class Hand(ABC):
    def __init__(self, game_strategy: GameStrategy) -> None:
        self.game_strategy: GameStrategy = game_strategy

    def getWinner(self, opponentHand: "Hand") -> str:
        return self.game_strategy.play(opponentHand)

    @abstractmethod
    def getName(self) -> None:
        pass
