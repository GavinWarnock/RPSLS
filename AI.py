import random
from player import Player

class AI(Player):
    def __init__(self):
        super().__init__()

    def ai_select_gesture(self):
        ai_gesture = random.choice(self.gesture)
        print ('AI chooses ', ai_gesture)
        return ai_gesture
    