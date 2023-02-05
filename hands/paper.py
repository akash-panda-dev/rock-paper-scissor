from constants.app_constants import PAPER
from game_strategy.game_strategy_interface import GameStrategy
from hands.hand_interface import Hand


class Paper(Hand):

    hand_name: str = PAPER

    def __init__(self, game_strategy: GameStrategy) -> None:
        super().__init__(game_strategy)

    def getName(self) -> str:
        return self.hand_name
