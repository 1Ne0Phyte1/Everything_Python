import pygame

# Initialize Pygame
pygame.init()

# Create a screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("wQ.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("wQ.png")
playerX = 370
playerY = 480
# Changing Value
playerX_change = 0

def player(x, y):
    # Player position
    screen.blit(playerImg, (x, y))


#  Game Loop
running = True
while running:
    # RGB
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Important to exit the game window
            running = False

        # if keystroke is pressed check whether it's right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.5
                #print("Left arrow is pressed!")
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.5
                #print("Right arrow is pressed!")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
                #print("KeyStroke has been released")


    # player
    #Movement
    playerX += playerX_change

    # Boundary
    if playerX <= 0:
        playerX = 736
    elif playerX >= 736:
        playerX = 0
    #Position
    player(playerX, playerY)

    # Updates the screen/Game
    pygame.display.update()
