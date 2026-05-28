import math
import random
import pygame

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27

# Initialize Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Clock controller for standard 60 FPS speed
clock = pygame.time.Clock()

# Fix Image Scales Automatically
background_raw = pygame.image.load('back2.png')
background = pygame.transform.scale(background_raw, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Caption and Icon
pygame.display.set_caption("Space Invader")
try:
    icon_raw = pygame.image.load('ufo.png')
    icon = pygame.transform.scale(icon_raw, (32, 32))
    pygame.display.set_icon(icon)
except:
    pass

# Scale Player (64x64 pixels)
playerImg_raw = pygame.image.load('player.png')
playerImg = pygame.transform.scale(playerImg_raw, (64, 64))

playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0

# Enemy Setup
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

enemyImg_raw = pygame.image.load('enemy.png')
enemyImg_scaled = pygame.transform.scale(enemyImg_raw, (64, 64))

for _i in range(num_of_enemies):
    enemyImg.append(enemyImg_scaled)
    enemyX.append(random.randint(0, SCREEN_WIDTH - 64))
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)

# =========================================================================
# KIDS LESSON: MAKING THE BULLET BIG & BOLD
# We double the dimensions from (16, 32) to (32, 64) so it's super visible!
# =========================================================================
bulletImg_raw = pygame.image.load('bullet.png')
bulletImg = pygame.transform.scale(bulletImg_raw, (32, 64))

bulletX = 0
bulletY = PLAYER_START_Y
bulletX_change = 0
bulletY_change = BULLET_SPEED_Y
bullet_state = "ready"

# Score Setup (Safe System Font)
score_value = 0
font = pygame.font.SysFont('Arial', 32, bold=True)
textX = 10
textY = 10

# Game Over Text
over_font = pygame.font.SysFont('Arial', 64, bold=True)

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (240, 220))

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    # LESSON FOR KIDS: Since our bullet is now 32px wide, we add 16 
    # to center it perfectly at the tip of our 64px ship (64 / 2 - 32 / 2 = 16)
    screen.blit(bulletImg, (x + 16, y)) 

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2)
    return distance < COLLISION_DISTANCE

# Game loop
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bulletX = playerX
                bulletY = PLAYER_START_Y 
                fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
            playerX_change = 0

    # Player Movement
    playerX += playerX_change
    playerX = max(0, min(playerX, SCREEN_WIDTH - 64))  

    # Enemy Movement & Logic
    for i in range(num_of_enemies):
        if enemyY[i] > 340:  # Game Over Condition
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0 or enemyX[i] >= SCREEN_WIDTH - 64:
            enemyX_change[i] *= -1
            enemyY[i] += enemyY_change[i]

        # Only check collision when the bullet is in flight
        if bullet_state == "fire" and isCollision(enemyX[i], enemyY[i], bulletX, bulletY):
            bulletY = PLAYER_START_Y
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, SCREEN_WIDTH - 64)
            enemyY[i] = random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)

        enemy(enemyX[i], enemyY[i], i)

    # Bullet Movement Logic
    if bullet_state == "fire":
        bulletY -= bulletY_change
        fire_bullet(bulletX, bulletY)
        
        # Reset if the laser reaches the top edge of the window
        if bulletY <= -32: # Changed to -32 so the large bullet flies completely out of sight before resetting
            bulletY = PLAYER_START_Y
            bullet_state = "ready"

    player(playerX, playerY)
    show_score(textX, textY)
    
    clock.tick(60) # Keep game at standard smooth speed
    pygame.display.update()

pygame.quit()
