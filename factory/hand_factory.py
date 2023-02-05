from constants.app_constants import PAPER, ROCK, SCISSORS
from factory.game_strategy_factory import GameStrategyFactory
from hands.hand_interface import Hand
from hands.paper import Paper
from hands.rock import Rock
from hands.scissors import Scissors


class HandFactory:
    def __init__(self, game_strategy_factory: GameStrategyFactory) -> None:
        self.game_strategy_factory: GameStrategyFactory = game_strategy_factory

    def __create_rock_hand(self) -> Rock:
        return Rock(self.game_strategy_factory.createRockGameStrategy())

    def __create_paper_hand(self) -> Paper:
        return Paper(self.game_strategy_factory.createPaperGameStrategy())

    def __create_scissors_hand(self) -> Scissors:
        return Scissors(self.game_strategy_factory.createScissorsGameStrategy())

    def get_hand(self, hand_name: str) -> Hand:
        if hand_name == ROCK:
            return self.__create_rock_hand()
        elif hand_name == PAPER:
            return self.__create_paper_hand()
        elif hand_name == SCISSORS:
            return self.__create_scissors_hand()
        else:
            raise ValueError(f"Unknown hand: {hand_name}")
