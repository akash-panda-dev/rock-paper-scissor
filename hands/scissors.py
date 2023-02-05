from constants.app_constants import SCISSORS
from game_strategy.game_strategy_interface import GameStrategy
from hands.hand_interface import Hand


class Scissors(Hand):

    hand_name: str = SCISSORS

    def __init__(self, game_strategy: GameStrategy) -> None:
        super().__init__(game_strategy)

    def getName(self) -> str:
        return self.hand_name
