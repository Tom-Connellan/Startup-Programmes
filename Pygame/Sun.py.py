import pygame


# - - Global Constnats

# - - Colours
Black = (0,0,0)
White = (255,255,255)
Blue = (50, 50, 255)
Yellow = (255, 255, 0)
Red = (255, 0, 0)
Brown = (98, 46, 0)
Green = (0, 153, 0)
L_Blue = (51, 153, 255)

# - - Time of day
Time = "Day"

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

# - - Creating the moving sun
x = -40
y = 240

### - - Game Loop
while not done:
    # - - User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #end if
    #next event
    # - - Game logic
    if -40 < x < 680:
        x = x + 1
        Time = "Day"

    elif x == 680:
        x = - 380
        Time = "Night"

    else:
        x = x + 1
        Time = "Night"

    if x < -40:
        y = 240
    elif x > 320:
        y = y + 0.5
    elif x == 320:
        y = y
    elif x < 320:
        y = y - 0.5

    # - - Screen backgorund
    screen.fill(Black)

    # - - Draw objects here
    if Time == "Day":
        pygame.draw.rect(screen, L_Blue, (0, 0, 640, 480))
    elif Time == "Night":
        pygame.draw.rect(screen, Blue, (0, 0, 640, 480))
    pygame.draw.rect(screen, White, (220, 165, 200, 150))
    pygame.draw.rect(screen, Brown, (305, 275, 30, 60))
    for count in range (240, 500, 130):
        for count2 in range (180, 450, 75):
            if Time == "Day":
                pygame.draw.rect(screen, Black, (count, count2, 30, 30))
            elif Time == "Night":
                pygame.draw.rect(screen, Yellow, (count, count2, 30, 30))
    pygame.draw.circle(screen, Yellow, (x, y), 40, 0)
    pygame.draw.rect(screen, Green, (0, (480-165), 640, 190))

    # - - Flip display to reveal new positio of objects
    pygame.display.flip()

    # - - Increase clock
    clock.tick(60)
#End While
pygame.quit()