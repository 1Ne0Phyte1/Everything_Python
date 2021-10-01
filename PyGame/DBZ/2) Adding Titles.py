import pygame

# Initialize Pygame
pygame.init()

#Create a screen
screen = pygame.display.set_mode((800,600))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("Cell.png")
pygame.display.set_icon(icon)

#  Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Important to exit the game window
            running = False

    # RGB
    screen.fill((255,0,0))
    pygame.display.update()