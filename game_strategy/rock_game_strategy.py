from game_strategy.game_strategy_interface import GameStrategy
from hands.hand_interface import Hand
from hands.paper import Paper
from hands.rock import Rock
from hands.scissors import Scissors


class RockGameStrategy(GameStrategy):

    def play(self, hand: Hand) -> str:
        if isinstance(hand, Rock):
            return "Its a draw!"

        if isinstance(hand, Paper):
            return "Paper beats rock!"

        if isinstance(hand, Scissors):
            return "Rock beats scissors!"

        raise ValueError(f"Hand {hand.getName()} is not a valid hand!")
