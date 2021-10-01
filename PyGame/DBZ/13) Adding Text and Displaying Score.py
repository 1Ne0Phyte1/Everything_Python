import pygame
import random
import math


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
enemyImg = []
enemyX = []
enemyY = []
# Changing Value
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.transform.scale(picture1, (50, 100)))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    # Changing Value
    enemyX_change.append(0.5)
    enemyY_change.append(40)

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

# score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def player(x, y):
    # Player position
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    # Player position
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


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
            if event.key == pygame.K_q:
                running = False

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
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]

        if enemyX[i] <= 0:
            enemyX_change[i] = 0.3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.3
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            # print(score_value)
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 100)

        enemy(enemyX[i], enemyY[i], i)

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # Position
    player(playerX, playerY)

    show_score(textX, textY)
    # Updates the screen/Game
    pygame.display.update()
