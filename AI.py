import random
from player import Player

class AI(Player):
    def __init__(self):
        super().__init__()

    def select_gesture(self):
        print ('AI chooses ', self.gesture)
        

    