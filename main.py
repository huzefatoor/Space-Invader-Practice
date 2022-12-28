# Creating game window
import pygame
import math
import random

# Initialize the pygame
pygame.init()

# This command will make the screen, inside the brackets is width, and height
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('2824536.jpg')

# Caption and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('space-ship.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
enemy_bulletX = []
enemy_bulletY = []
enemy_bullet_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('ufo.png'))
    enemyX.append(random.randint(0, 800))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(2)
    enemyY_change.append(40)

# Bullet

# ready = you can't see the bullet on the screen 
# Fire = The bullet is shooting
bulletImg = pygame.image.load('laser.png')
bulletX = 0
bulletY = 480
bulletX_change = 2
bulletY_change = 10
bullet_state = "ready"

# Enemy Bullet
enemy_bulletImg = pygame.image.load('001-laser.png')
enemy_bulletX = enemyX
enemy_bulletY = enemyY
enemy_bulletX_change = enemyX_change
enemy_bulletY_change = enemyY_change
enemy_bullet_state = "ready"

# Score

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10


def enemy_hit(x, y):
    global enemy_bullet_state
    enemy_bullet_state = "fire"
    screen.blit(enemy_bulletImg, (x, y))



def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (250, 200, 0))
    screen.blit(score, (x, y))

# shows the player on the screen
def player(x, y):
    screen.blit(playerImg, (x, y))

# shows the enemy on the screen
def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def Collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2))
    if distance < 27:
        return True
    else:
        return False


# Game loop
# If running is true, then the window will continue to run,
# if false (as in the player stops the game) the game stops running
running = True
while running:
    # background
    # RGB = RED, GREEN, BLUE
    screen.fill((0, 0, 0))
    # Background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If keystroke is pressed check if it is right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -3
            if event.key == pygame.K_RIGHT:
                playerX_change = 3
            if event.key == pygame.K_SPACE:
                # get the current coordinate of the spaceship
                if bullet_state == "ready":
                    bulletX = playerX
                fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # 5 = 5 + -0.1 -> 5 = 5 - 0.1
    # 5 = 5 + 0.1

    # checking for boundaries of movement
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy movement
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
        enemy_bulletX[i] == enemyX[i]
        enemy_bulletY[i] == enemyY[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 2
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -2
            enemyY[i] += enemyY_change[i]
        if enemy_bullet_state == "ready":
            enemy_hit(enemy_bulletX[i], enemy_bulletY[i])


        # collision on enemy spaceship
        collision = Collision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bullet_state = "ready"
            bulletY = playerY
            score_value += 1
            explosionImg = pygame.image.load('001-explosion.png')
            explodeX = enemyX[i]
            explodeY = enemyY[i]
            screen.blit(explosionImg, (enemyX[i], enemyY[i]))
            enemyX[i] = random.randint(0, 800)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # Enemy bullet movement
    if enemy_bulletY[i] <= enemyY[i]:
        enemy_bulletY[i] = enemyY[i]
        enemy_bullet_state == "ready"
    if enemy_bullet_state == "fire":
        enemy_hit(enemy_bulletX[i], enemy_bulletY[i])




    # Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change


    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
