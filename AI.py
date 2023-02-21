import random
from player import Player

class AI(Player):
    def __init__(self):
        super().__init__()

    def choose_gesture(self):
        print ('AI chooses ', random.choice(self.gesture))
        self.point += 1

    