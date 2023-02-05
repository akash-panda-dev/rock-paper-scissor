from game_strategy.paper_game_strategy import PaperGameStrategy
from game_strategy.rock_game_strategy import RockGameStrategy
from game_strategy.scissors_game_strategy import ScissorsGameStrategy


class GameStrategyFactory:
    def __init__(self) -> None:
        pass

    def createRockGameStrategy(self) -> RockGameStrategy:
        return RockGameStrategy()

    def createPaperGameStrategy(self) -> PaperGameStrategy:
        return PaperGameStrategy()

    def createScissorsGameStrategy(self) -> ScissorsGameStrategy:
        return ScissorsGameStrategy()
