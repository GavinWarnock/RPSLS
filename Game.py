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

def select_players(self):
    print("")
    amount_of_players = input("How many players? 1 or 2  ")
    if amount_of_players == "1":
        print("")
        print("1 player selected!")
        print("Player 1")
        Human.select_gesture(self)
    elif amount_of_players == "2":
        print("")
        print("2 players selected!")
        print("Player 1")
        Human.select_gesture(self)
        print("")
        print("Player 2")
    else:
        "Please select 1 or 2"

def game():
    

select_players()
