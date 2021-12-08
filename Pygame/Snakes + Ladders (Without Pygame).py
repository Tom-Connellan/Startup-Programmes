import random

Done = False

players = []

#Creating lists for the start and end of the Snakes/Ladders
Snake_Ladder_Start = [2, 10, 20, 40, 36, 55, 69, 82, 85, 23, 34, 54, 48, 66, 79, 85, 95, 99]

Snake_Ladder_End = [50, 21, 34, 58, 75, 60, 83, 96, 90, 12, 22, 40, 31, 50, 65, 70, 20, 87]

#Creating an empty list for
Snake_Ladder = []

#Finding how many people are people are playing
num_players = int(input("How many people are playing? "))


#### Player Class
class Player():
    def __init__(self,n):
        self.position = 0
        self.name = n

    #Moving the player - Increasing place by value between 1 and 6    
    def update_pos(self,p):
        self.position = p

    def get_pos(self):
        return self.position

    def get_name(self):
        return self.name

##### Player Classs

class Dice():
    def __init__(self):
        self.faces = 6

    def roll_dice(self):
        return random.randint(1,self.faces)

### Dice class

#Board class, contains the size of the board + checks if they reach the end
class Board():

    def __init__(self,number_of_players):
       
        self.size = 100
       # add players
        self.player_list = []
        for count in range(number_of_players):
            name = input("What is the name of player")
            p = Player(name)
            self.player_list.append(p)

        self.dice = Dice()

    def game_play(self):
        
        for p in self.player_list:
            move = self.dice.roll_dice()
            p.update_pos(p.get_pos() + move)
            print (p.get_name(), p.get_pos())
            if p.get_pos() > self.size:
                return True

        
        for count in range(0, 18):
            if p.get_pos() == Snake_Ladder_Start[count]:
                if Snake_Ladder_Start[count] > Snake_Ladder_End[count]:
                   print(p.get_name(), "hit a snake!")
                else:
                    print(p.get_name(), "hit a ladder!")
                p.update_pos(p.get_pos() + int(Snake_Ladder_End[count]))
        #print(self, ":", self.position)

   #def update_game():


### Main game starts here
b = Board(2)

#Game loop
while Done == False:
    
    print("Press ENTER to roll")

    input()

    res = b.game_play()
    if res == True:
        Done = True

print("END GAME")