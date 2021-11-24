import pygame
import random
import math

from pygame.constants import QUIT

# - - Global Constants

# - - Colours
Black = (0,0,0)
White = (255,255,255)
Blue = (50, 50, 255)
Yellow = (255, 255, 0)
Red = (255, 0, 0)
Brown = (98, 46, 0)
Green = (0, 153, 0)
L_Blue = (51, 153, 255)

# - - Initialise Pygame
pygame.init()

# - - Creating the loop
done = False

# Invader image
#invaderIMG = pygame.image.load('invader.png')

# - - Blank Screen
size = (640, 480)
screen = pygame.display.set_mode(size)

#Creating the size of the player and the invader
player_x = 20
player_y = 20
invader_x = 10
invader_y = 10
bullet_x = 2
bullet_y = 2
player_pos_x = 20
player_pos_y = 20

bullet_count = 0

# - - Title of new window/screen
pygame.display.set_caption("Space Invaders")

# - - Define the class Invader
class Invader(pygame.sprite.Sprite):
    #Define the constructor for invader (all attributes of the invaders
    def __init__(self, color, width, height, speed):
        # The sprite instructor
        super().__init__()
        # Create the sprite and fill it with colour
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        # Set speed of the sprite
        self.speed = speed
        # Position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0,640)
        self.rect.y = random.randrange(-50, 0)
    

    # Class update function - runs for each pass through the game loop
    def update(self):
        if self.rect.y > 480:
            self.rect.y = -5
            self.rect.x = random.randrange(0, 640)
        else:
            self.rect.y = self.rect.y + self.speed

    # Class update funciton - draws everything for every loop

# - - Define the class Player
class Player(pygame.sprite.Sprite):
    #Define the constructor for the player
    def __init__(self, color, width, height):
        #lives, bullet_count):
        #The sprite constructor
        super().__init__()
        #Create the sprite and fill it with colour
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        # Position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = (size[0] - player_x) / 2
        self.rect.y = size[1] - player_y
        self.bullet_count = 50
    
    # Moving the player + firing bullets
    def update(self):
        keys = pygame.key.get_pressed()
            ## - the left or right key has been pressed
        if keys[pygame.K_LEFT]:
            if self.rect.x != 0:
                self.rect.x = self.rect.x - 5
            elif self.rect.x == 0:
                self.rect.x = self.rect.x
            
        if keys[pygame.K_RIGHT]:
            if self.rect.x + 20 != 640:
                self.rect.x = self.rect.x + 5
            elif self.rect.x + 20 == 640:
                self.rect.x = self.rect.x

        if keys[pygame.K_UP]:
            #if self.bullet_count == 0:
            self.shootbullet()

    def shootbullet(self):
        # Creating my bullet
        my_bullet = Bullet(White, 2, 2, self.rect.x, 470)
        all_sprites_group.add(my_bullet)



    # - - When invader hits player add 5 to the score
    #player_hit_group = pygame.sprite.spritecollide(Player, Invader, True)
    #for foo in player_hit_group:
    #    Player.lives = Player - 1


# - - Define the class Bullet
class Bullet(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x_pos, y_pos):
        #The sprite instructor
        super().__init__()
        #Create the sprite 
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        #Starting position of bullets
        self.x_pos = self.rect.x
        self.rect.y = 470

    # Class update function - draws everything for every loop
    def update(self):
        #Moving all bullets upwards by 1
        if self.rect.y < - 2:
            self.rect.y = -3
        else:
            self.rect.y = self.rect.y - 1


# Create a list of the invaders
Invader_group = pygame.sprite.Group()

#Create a list of the bullets
Bullet_group = pygame.sprite.Group()

#Create a list of all sprites
all_sprites_group = pygame.sprite.Group()

# Creating my player 
my_player = Player(Red, player_x, player_y)
all_sprites_group.add(my_player)

#Creating the invaders
number_of_invaders = 10
for count in range(number_of_invaders):
    # Dimensions of the invader
    my_invaders = Invader(Blue, invader_x, invader_y, 1)
    #my_invaders = screen.blit(invaderIMG, (invader_x, invader_y), 1)
    Invader_group.add (my_invaders)
    all_sprites_group.add (my_invaders)

# - - Manages how fast screen refreshes
clock = pygame.time.Clock()

### - - Game Loop
while done == False:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            done = True
        # End if

    #Next event

    # - - Game logic goes in here
    all_sprites_group.update()

    # - - Screen backgorund
    screen.fill(Black)

    # - - Draw here
    all_sprites_group.draw (screen)

    # - - Flip display to reveal new position of objects
    pygame.display.flip()

    # - - Increase clock
    clock.tick(60)
    
#End While
pygame.quit()