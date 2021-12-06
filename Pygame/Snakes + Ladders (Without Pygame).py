import random

Done = False

players = []

Snake_Ladder_Start = [2, 10, 20, 40, 36, 55, 69, 82, 85, 23, 34, 54, 48, 66, 79, 85, 95, 99]

Snake_Ladder_End = [50, 21, 34, 58, 75, 60, 83, 96, 90, 12, 22, 40, 31, 50, 65, 70, 20, 87]

Snake_Ladder = []

num_players = int(input("How many people are playing? "))

class Board():

    def __init__(self, size):
       self.size = 100

    def update_game():
        Player.roll()

        for count in range(1, 18):
            if Player.position == Snake_Ladder_Start[count]:
                Player.position = Snake_Ladder_End[count]

        for count in range(1, num_players):
            Player.position = Player.roll(Player.position)
            print(players[count], ":", Player.position)


class Player():
    def __init__(self, name, position):
        self.name = self.name
        self.position = 0

    #Moving the player - Increasing place by value between 1 and 6    
    def update(self):
        self.position = self.roll(self.position)
        print(self, self.position)
        if self.position >= Board.size:
            print("Player", self.name, "wins!")
            Done = True

    def roll(position):
       position = position + random.randint(1,6)

class S_L():
    def __init__(self, name, start, finish):
        self.start = self.start
        self.end = self.end
        
for count in range(1, 18):
    if Player.position == Snake_Ladder_Start[count]:
        Player.position = Snake_Ladder_End[count]
            
for count in range(1, 18):
    Snake_Ladder = S_L()
    S_L.end = Snake_Ladder_End[count]
    S_L.start = Snake_Ladder_Start[count]

for count in range(1, num_players):
    players.append(Player(count))
    
b = Board()

while Done == False:
    
    print("Press ENTER key to roll")

    input()

    b.update_game()