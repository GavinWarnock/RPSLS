from human import Human
from AI import AI

class Game:
    def __init__(self):
        self.player_one = Human("Player 1")
        self.player_two = Human("Player 2")
        self.ai_player = AI()

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
            print("Single-player selected!")
            p1_points = 0
            p2_points = 0
            while p1_points != 2 or p2_points != 2:
                if p1_points >= 2:
                    print("Player 1 WINS!")
                    break
                elif p2_points >= 2:
                    print("Player 2 WINS!")
                    break
                print("Player one please choose your gesture!")
                p1_choice = self.player_one.select_gesture()
                p2_choice = self.ai_player.ai_select_gesture()
                if p1_choice == p2_choice:
                    print("It's a Tie!")
                elif p1_choice == "Rock" and (p2_choice == "Paper" or p2_choice == "Spock"):
                        print("Player 2 has won the round!")
                        p2_points += 1
                  
                elif p1_choice == "Paper" and (p2_choice == "Scissors" or p2_choice == "Lizard"):
                        print("Player 2 has won the round!")
                        p2_points += 1
                    
                elif p1_choice == "Scissors" and (p2_choice == "Rock" or p2_choice == "Spock"):
                        print("Player 2 has won the round!")
                        p2_points += 1

                elif p1_choice == "Lizard" and (p2_choice == "Rock" or p2_choice == "Scissors"):
                        print("Player 2 has won the round!")
                        p2_points += 1

                elif p1_choice == "Spock" and (p2_choice == "Paper" or p2_choice == "Lizard"):
                        print("Player 2 has won the round!")
                        p2_points += 1
                else:
                    print("Player 1 has won the round!")
                    p1_points += 1        
        elif amount_of_players == "2":
            print("")
            print("Multi-player selected!")
            p1_points = 0
            p2_points = 0
            while p1_points != 2 or p2_points != 2:
                if p1_points >= 2:
                    print("Player 1 WINS!")
                    break
                elif p2_points >= 2:
                    print("Player 2 WINS!")
                    break
                print("Player one please choose your gesture!")
                p1_choice = self.player_one.select_gesture()
                print("Player two please choose your gesture!")
                p2_choice = self.player_two.select_gesture()
                if p1_choice == p2_choice:
                    print("It's a Tie!")
                elif p1_choice == "Rock" and (p2_choice == "Paper" or p2_choice == "Spock"):
                        print("Player 2 has won the round!")
                        p2_points += 1
                  
                elif p1_choice == "Paper" and (p2_choice == "Scissors" or p2_choice == "Lizard"):
                        print("Player 2 has won the round!")
                        p2_points += 1
                    
                elif p1_choice == "Scissors" and (p2_choice == "Rock" or p2_choice == "Spock"):
                        print("Player 2 has won the round!")
                        p2_points += 1

                elif p1_choice == "Lizard" and (p2_choice == "Rock" or p2_choice == "Scissors"):
                        print("Player 2 has won the round!")
                        p2_points += 1

                elif p1_choice == "Spock" and (p2_choice == "Paper" or p2_choice == "Lizard"):
                        print("Player 2 has won the round!")
                        p2_points += 1
                else:
                    print("Player 1 has won the round!")
                    p1_points += 1 
        else:
            "Please select 1 or 2"


