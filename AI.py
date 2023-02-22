import random
from player import Player

class AI(Player):
    def __init__(self):
        super().__init__()

    def select_gesture(self):
        ai_gesture = random.choice(self.gesture)
        print ('AI chooses ', random.choice(self.gesture))
        self.point += 1
        return ai_gesture
    