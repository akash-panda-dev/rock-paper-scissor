
from constants.app_constants import ROCK
from game_strategy.game_strategy_interface import GameStrategy
from hands.hand_interface import Hand



class Rock(Hand):

    hand_name: str = ROCK

    def __init__(self, game_strategy: GameStrategy) -> None:
        super().__init__(game_strategy)

    def getName(self) -> str:
        return self.hand_name
