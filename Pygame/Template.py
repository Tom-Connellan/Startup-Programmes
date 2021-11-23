import pygame

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

# - - Exit game flag set to false
done = False

# - - Manages how fast screen refreshes
clock = pygame.time.Clock()

### - - Game Loop
while done == False:

    # - - Screen backgorund
    screen.fill(Black)

    # - - Flip display to reveal new position of objects
    pygame.display.flip()

    # - - Increase clock
    clock.tick(60)
    
#End While
pygame.quit()