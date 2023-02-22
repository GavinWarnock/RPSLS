from human import Human
from AI import AI

class Game:
    def __init__(self):
        self.human = Human()
        self.AI = AI()

    def display_greeting(self):
        print("Welcome to RPSLS or Rock, Paper, Scissors, Lizard, Spock")
        print("")
        print("Each match will be a best of three games.")
        print("Use the number keys to enter your selection.")
        print("")
        print("Scissors cut Paper")
        print("Paper covers Rock")
        print("Rock crushes Lizard")
        print("Lizard poisons Spock")
        print("Spock smashes Scissors")
        print("Scissors decpitates Lizard")
        print("Lizard eats Paper")
        print("Paper disproves Spock")
        print("Spock vaporizes Rock")
        print("Rock crushes Scissors")
  
def game_rounds(self):
    amount_of_players = input("How many players? 1 or 2  ")
    if amount_of_players == "1":
        print("")
        print("1 player selected!")
        p1_points = 0
        ai_points = 0
        while p1_points != 0 or ai_points != 0:
            print("Player one please choose your gesture!")
            Human.select_gesture()
            AI.select_gesture()
            print(f"The ai chooses {ai_gesture}")
    elif amount_of_players == "2":
        print("")
        print("2 players selected!")
        p1_points = 0
        p2_points = 0
        while p1_points !=2 or p2_points != 2:
            

    else:
        "Please select 1 or 2"
   
        
 



