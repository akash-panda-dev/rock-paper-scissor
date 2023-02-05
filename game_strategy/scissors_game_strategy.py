from game_strategy.game_strategy_interface import GameStrategy
from hands.hand_interface import Hand
from hands.paper import Paper
from hands.rock import Rock
from hands.scissors import Scissors


class ScissorsGameStrategy(GameStrategy):

    def play(self, hand: Hand) -> str:
        if isinstance(hand, Rock):
            return "Rock beats scissors!"

        if isinstance(hand, Paper):
            return "Scissors beats paper!"

        if isinstance(hand, Scissors):
            return "It's a draw!"

        raise ValueError(f"Hand {hand.getName()} is not a valid hand!")
