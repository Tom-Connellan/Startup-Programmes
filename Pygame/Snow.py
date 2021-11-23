import pygame
import random
import math

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

# - - Blank Screen
size = (640, 480)
screen = pygame.display.set_mode(size)

# - - Title of new window/screen
pygame.display.set_caption("My Window")

# - - Define the class snow
class Snow(pygame.sprite.Sprite):
    #Define the constructor for snow (all attributes of the snowflakes)
    def __init__(self, color, width, height, speed):
        # The sprite instructor
        super().__init__()
        # Create the sprite and fill it with colour
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        # Set speed of the sprite
        self.speed = speed
        #Position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0,640)
        self.rect.y = random.randrange(0,480)
    

    # Class update function - runs for each pass through the game loop
    def update(self):
        if self.rect.y > 480:
            self.rect.y = -5
            self.rect.x = random.randrange(0, 640)
        else:
            self.rect.y = self.rect.y + self.speed



# Create a list of the snow flakes
Snow_group = pygame.sprite.Group()

#Create a list of all sprites
all_sprites_group = pygame.sprite.Group()
    
    
#Creating the snowflakes
number_of_flakes = 50
for count in range(number_of_flakes):
    my_snow = Snow(White, 5, 5, 10)
    Snow_group.add (my_snow)
    all_sprites_group.add (my_snow)

# - - Exit game flag set to false
done = False

# - - Manages how fast screen refreshes
clock = pygame.time.Clock()

### - - Game Loop
while done == False:

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