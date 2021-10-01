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


def player(x,y):
    #Player position
    screen.blit(playerImg, (x, y))


#  Game Loop
running = True
while running:
    # RGB
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Important to exit the game window
            running = False

    # player
    #Here we are ging value for the position to see how the player moves
    playerX += 0.5
    playerY -= 0.5

    player(playerX,playerY)

    # Updates the screen/Game
    pygame.display.update()
