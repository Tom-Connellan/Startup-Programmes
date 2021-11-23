import pygame

# - - Global Constants
ball_width = 20
x_val = 10
y_val = 10
x_direction = 1
y_direction = 1
padd_length = 15
padd_width = 600
x_padd = 0
y_padd = 20
score = 10
done = False

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
    
    pygame.draw.rect(screen, Blue, (x_val, y_val, ball_width, ball_width))
    pygame.draw.rect(screen, White, (x_padd, y_padd, padd_length, padd_width))

    if x_val == 620:
        x_direction = x_direction * -1
    elif x_val == 0:
        x_direction = x_direction * -1

    if y_val == 0:
        y_direction = y_direction * -1
    elif y_val == 460:
        y_direction = y_direction * -1

    for count in range (1, 60):
        if x_val == 15:
            if y_padd + count == y_val:
                x_direction = x_direction * -1
    
    if x_val == 0:
        x_val = 150
        y_val = 200
        score = score - 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #End If
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                # logic of key press
                if y_padd  != 0:
                    y_padd = y_padd - 5
                elif y_padd == 0:
                    y_padd = y_padd
            elif event.key == pygame.K_DOWN:
                #logic of down key press
                if y_padd + 60 != 480:
                    y_padd = y_padd + 5
                elif y_padd == 480:
                    y_padd = y_padd
                
        
    keys = pygame.key.get_pressed()
        ## - the up key or down key has been pressed
    if keys[pygame.K_UP]:
        if y_padd != 0:
            y_padd = y_padd - 5
        elif y_padd == 0:
            y_padd = y_padd
        
    if keys[pygame.K_DOWN]:
        if y_padd + 60 != 480:
            y_padd = y_padd + 5
        elif y_padd + 60 == 480:
            y_padd = y_padd

    x_val = x_val + x_direction
    y_val = y_val + y_direction

    if score == 0:
        done = True

    # - - Flip display to reveal new position of objects
    pygame.display.flip()

    # - - Increase clock
    clock.tick(60)
#End While
pygame.quit()