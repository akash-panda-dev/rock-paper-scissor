from enum import Enum
from typing import Any

import gradio as gr

from constants.app_constants import PAPER, ROCK, SCISSORS
from factory.game_strategy_factory import GameStrategyFactory
from factory.hand_factory import HandFactory
from hands.hand_interface import Hand

hand_labels = [ROCK, PAPER, SCISSORS]
# Use hand names to add logic for the game

# Define a User enum
class User(Enum):
    HUMAN = 1
    AI = 2


from fastai.vision.all import *  # type: ignore

learn = load_learner("export.pkl")


class RockPaperScissors:
    def __init__(self):
        self.hand_factory: HandFactory = HandFactory(GameStrategyFactory())

    def getRCPWinner(self, human_hand_image_path) -> str:
        human_hand_image = PILImage.create(human_hand_image_path)

        user_hand = self.__get_hand_for_user(User.HUMAN, human_hand_image)  # type: ignore
        ai_hand = self.__get_hand_for_user(User.AI, human_hand_image)  # type: ignore
        winner = user_hand.getWinner(ai_hand)

        return f"<p>I have {ai_hand.getName()} <br> {winner}</p>"

    def __get_hand_for_user(
        self,
        user: User,
        hand_image: PILImage,
    ) -> Hand:
        if user == User.AI:
            return self.hand_factory.get_hand(random.choice(hand_labels))  # type: ignore
        else:
            pred = learn.predict(hand_image)
            return self.hand_factory.get_hand(pred[0])


if __name__ == "__main__":
    title = "Rock Paper Scissors AI"
    description = "A simple rock paper scissors game with AI"
    examples = ["Rock-Paper-Scissors/validation/rock7.png"]
    interpretation = "default"
    enable_queue = True

    webcam = gr.inputs.Image(shape=(640, 480), source="webcam")
    rock_paper_scissors = RockPaperScissors()

    gr.Interface(
        fn=rock_paper_scissors.getRCPWinner,
        inputs=webcam,
        outputs=gr.outputs.HTML(),
        title=title,
        description=description,
        examples=examples,
        interpretation=interpretation,
        enable_queue=enable_queue,
    ).launch()
