# from Game import Game
from human import Human

player_one = Human()
player_one.chosen_guesture = ('Choose your gesture')

def select_gesture(self):
        print("Choose 0 for Rock")
        print("Choose 1 for Paper")
        print("Choose 2 for Scissors")
        print("Choose 3 for Lizard")
        print("Choose 4 for Spock")
        print("")
        
        chosen_gesture = input("Choose your gesture.  ")
        

        for gesture in self.gesture:
            if gesture == self.gesture[0]:
                print(f'{self.player_one} chooses Rock')
                
            elif gesture == (self.gesture[1]):
                print(f'{self.player_one} chooses Paper')

            elif gesture == (self.gesture[2]):
                print(f'{self.player_one} chooses Scissors')

            elif gesture == (self.gesture[3]):
                print(f'{self.player_one} chooses Lizard')
                
            elif gesture == (self.gesture[4]):
                print(f'{self.player_one} chooses Spock')

        return chosen_gesture
       
select_gesture()

