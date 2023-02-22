from player import Player

class Human(Player):
    def __init__(self):
        self.player = 'Player'
        super().__init__()

    def select_gesture(self):
        print("Choose 0 for Rock")
        print("Choose 1 for Paper")
        print("Choose 2 for Scissors")
        print("Choose 3 for Lizard")
        print("Choose 4 for Spock")
        print("")
        
        
        valid_input = False

        while valid_input == False:
            chosen_gesture = int(input("Choose your gesture.  "))
            if chosen_gesture == 0:
                print(f"{self.player} has chosen Rock")
                return "Rock"
            elif chosen_gesture == 1:
                print(f"{self.player} has chosen Paper")
                return "Paper"
            elif chosen_gesture == 2:
                print(f"{self.player} has chosen Scissors")
                return "Scissors"
            elif chosen_gesture == 3:
                print(f"{self.player} has chosen Lizard")
                return "Lizard"
            elif chosen_gesture == 4:
                print(f"{self.player} has chosen Spock")
                return "Spock"
            else:
                print("Please select a valid gesture")
           
       # self.point += 1