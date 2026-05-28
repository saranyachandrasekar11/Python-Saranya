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
COLLISION_DISTANCE = 35  # Set to fit our perfectly scaled 64x64 sprites

# Initialize Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# =========================================================================
# LESSON 1: THE GAME TRAFFIC CONTROLLER
# This clock caps the game loop at 60 FPS so enemies move at human speeds.
# =========================================================================
clock = pygame.time.Clock()

# =========================================================================
# LESSON 2: FITTING THE BACKGROUND IMAGE
# This stretches any 'background1.png' picture to perfectly fill the screen.
# =========================================================================
background_raw = pygame.image.load('spback.png')
background = pygame.transform.scale(background_raw, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Caption and Icon
pygame.display.set_caption("Space Invader")
try:
    icon_raw = pygame.image.load('ufo.jpg')
    icon = pygame.transform.scale(icon_raw, (32, 32))  # Standard small icon size
    pygame.display.set_icon(icon)
except:
    pass

# =========================================================================
# LESSON 3: FITTING THE PLAYER SHIP
# This forces the player's image to shrink/grow into a clean 64x64 pixel box.
# =========================================================================
playerImg_raw = pygame.image.load('spaceshippp.png')
playerImg = pygame.transform.scale(playerImg_raw, (64, 64))

playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0

# Enemy Setup Lists
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

# =========================================================================
# LESSON 4: FITTING THE ALIEN INVADERS
# This resizes 'invader.png' down to 64x64 pixels BEFORE the game loop 
# copies it into our enemy swarm list.
# =========================================================================
enemyImg_raw = pygame.image.load('invaderrr.png')
enemyImg_scaled = pygame.transform.scale(enemyImg_raw, (64, 64))

for _i in range(num_of_enemies):
    enemyImg.append(enemyImg_scaled)
    enemyX.append(random.randint(0, SCREEN_WIDTH - 64))  
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)

# =========================================================================
# LESSON 5: FITTING THE BULLET IMAGE
# This makes the laser projectile big, bright, and easy to see on screen.
# =========================================================================
bulletImg_raw = pygame.image.load('bullettt.png')
bulletImg = pygame.transform.scale(bulletImg_raw, (32, 64))

bulletX = 0
bulletY = PLAYER_START_Y
bulletX_change = 0
bulletY_change = BULLET_SPEED_Y
bullet_state = "ready"

# Score Setup (Using Arial system font so it never crashes)
score_value = 0
font = pygame.font.SysFont('Arial', 32, bold=True)
textX = 10
textY = 10

# Game Over Text Setup
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
    # Plus 16 centers our 32-pixel bullet perfectly with the 64-pixel ship!
    screen.blit(bulletImg, (x + 16, y))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2)
    return distance < COLLISION_DISTANCE

# --- MAIN CORE GAME LOOP ---
running = True
while running:
    # Clear screen and render background first
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    # Event Input Processing
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
                bulletY = PLAYER_START_Y  # Fixes the bug where bullets didn't reset height
                fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
            playerX_change = 0

    # Player Movement Engineering
    playerX += playerX_change
    playerX = max(0, min(playerX, SCREEN_WIDTH - 64))  

    # Enemy Processing Loop
    for i in range(num_of_enemies):
        if enemyY[i] > 340:  # Game Over Boundary Check
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0 or enemyX[i] >= SCREEN_WIDTH - 64:
            enemyX_change[i] *= -1
            enemyY[i] += enemyY_change[i]

        # Fixes structural bullet bug by verifying it's actively in the 'fire' state
        if bullet_state == "fire" and isCollision(enemyX[i], enemyY[i], bulletX, bulletY):
            bulletY = PLAYER_START_Y
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, SCREEN_WIDTH - 64)
            enemyY[i] = random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)

        enemy(enemyX[i], enemyY[i], i)

    # Bullet Movement Engine
    # Moves the math block first, then fires it, so it's fully visible
    if bullet_state == "fire":
        bulletY -= bulletY_change
        fire_bullet(bulletX, bulletY)
        
        # Reset if the laser reaches the top edge of the screen layout
        if bulletY <= -32:
            bulletY = PLAYER_START_Y
            bullet_state = "ready"

    # Draw final renders over background
    player(playerX, playerY)
    show_score(textX, textY)
    
    # Tick the clock block to enforce 60FPS velocity regulations
    clock.tick(60)
    pygame.display.update()

pygame.quit()
