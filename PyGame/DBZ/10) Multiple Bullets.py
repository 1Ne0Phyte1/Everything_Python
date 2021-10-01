import pygame
import random

# Initialize Pygame
pygame.init()

# Create a screen
screen = pygame.display.set_mode((800, 600))

# BackGround
bg = pygame.image.load("BG.jpg")
background = pygame.transform.scale(bg, (800, 800))
# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("Goku.png")
pygame.display.set_icon(icon)

# Player
picture = pygame.image.load("Goku.png")
playerImg = pygame.transform.scale(picture, (50, 100))
playerX = 370
playerY = 480
# Changing Value
playerX_change = 0

# Enemy
picture1 = pygame.image.load("Cell.png")
enemyImg = pygame.transform.scale(picture1, (50, 100))
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
# Changing Value
enemyX_change = 0.5
enemyY_change = 40

# Bullet
picture2 = pygame.image.load("Kame.png")
bulletImg = pygame.transform.scale(picture2, (50, 100))
bulletX = 0
bulletY = 480
# Changing Value
bulletX_change = 0
bulletY_change = 2
# 'ready' state means - you cannot see the bullet on the screen
bullet_state = "ready"


def player(x, y):
    # Player position
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    # Player position
    screen.blit(enemyImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x, y + 10))


#  Game Loop
running = True
while running:
    # RGB
    screen.fill((100, 200, 255))
    # Background
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Important to exit the game window
            running = False

        # if keystroke is pressed check whether it's right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.5
                # print("Left arrow is pressed!")
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.5
                # print("Right arrow is pressed!")
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    # Get current x coordinate of Goku
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)



        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
                # print("KeyStroke has been released")

    # Player Boundary
    # Movement
    playerX += playerX_change

    if playerX <= 0:
        playerX = 736
    elif playerX >= 736:
        playerX = 0

    # Boundary Enemy / movement
    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 0.3
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.3
        enemyY += enemyY_change

    #Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -=bulletY_change



    # Position
    player(playerX, playerY)
    enemy(enemyX, enemyY)

    # Updates the screen/Game
    pygame.display.update()
