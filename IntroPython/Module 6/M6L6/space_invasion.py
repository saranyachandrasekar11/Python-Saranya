import pygame
import random
import math
import sys
import os
import urllib.request

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# --- AUTOMATIC ASSET DOWNLOADER ---
# This dictionary maps local filenames to public hosting links for the exact matching graphics assets
ASSETS = {
    "background.png": "https://unsplash.com", # Starfield
    "player.png": "https://ibb.co",      # White & Red Retro Rocket Ship
    "enemy.png": "https://ibb.co",    # Orange Pixel Alien Invader
    "bullet.png": "https://ibb.co"       # Yellow Laser Beam Strip
}

def download_assets():
    """Checks for assets locally; if missing, downloads them automatically."""
    print("Checking game assets...")
    for filename, url in ASSETS.items():
        if not os.path.exists(filename):
            print(f"Downloading missing asset: {filename}...")
            try:
                # Custom User-Agent header string to bypass standard bot blocks
                req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req) as response, open(filename, 'wb') as out_file:
                    out_file.write(response.read())
            except Exception as e:
                print(f"Failed to download {filename} from server. Error: {e}")
                # Create structural backup color block surfaces if network times out
                surf = pygame.Surface((64, 64))
                surf.fill((255, 0, 0))
                pygame.image.save(surf, filename)

# Trigger download layer before initiating window contexts
download_assets()

# Initialize Pygame engine tools
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invader - Image Edition")
clock = pygame.time.Clock()

# Fonts
font = pygame.font.SysFont("Arial", 36, bold=True)
game_over_font = pygame.font.SysFont("Arial", 64, bold=True)

# Load Images safely and conform sizing parameters exactly
background = pygame.transform.scale(pygame.image.load('background.png'), (SCREEN_WIDTH, SCREEN_HEIGHT))
playerImg = pygame.transform.scale(pygame.image.load('player.png'), (60, 60))
enemyImg = pygame.transform.scale(pygame.image.load('enemy.png'), (55, 45))
bulletImg = pygame.transform.scale(pygame.image.load('bullet.png'), (12, 32))

# --- GAME SPRITE ENTITIES ---
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = playerImg
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 60))
        self.speed = 6

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
        # Boundaries locking
        self.rect.left = max(0, self.rect.left)
        self.rect.right = min(SCREEN_WIDTH, self.rect.right)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemyImg
        self.rect = self.image.get_rect()
        self.reset_position()
        self.direction = random.choice([-1, 1])
        self.speed_x = 3
        self.speed_y = 35

    def reset_position(self):
        self.rect.x = random.randint(50, SCREEN_WIDTH - 100)
        self.rect.y = random.randint(50, 180)

    def update(self):
        self.rect.x += self.speed_x * self.direction
        if self.rect.right >= SCREEN_WIDTH or self.rect.left <= 0:
            self.direction *= -1
            self.rect.y += self.speed_y

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = bulletImg
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 12

    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()

# Sprite Tracking Directories
all_sprites = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

# Populate the swarm layout matching the reference graphic image frame
for _ in range(5):
    invader = Enemy()
    all_sprites.add(invader)
    enemy_group.add(invader)

# Track parameters
score = 0
game_over = False

# --- MAIN RENDER CYCLE LOOP ---
running = True
while running:
    # Render static structural visual background framework layers first
    screen.blit(background, (0, 0))

    # Event Processing Interactivity Layer
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                if len(bullet_group) < 3: # Multi-shot constraint thresholds 
                    laser = Bullet(player.rect.centerx, player.rect.top)
                    all_sprites.add(laser)
                    bullet_group.add(laser)
            elif event.key == pygame.K_r and game_over:
                # Reset Environment matrices parameters fully
                score = 0
                game_over = False
                all_sprites.empty()
                enemy_group.empty()
                bullet_group.empty()
                player = Player()
                all_sprites.add(player)
                for _ in range(5):
                    invader = Enemy()
                    all_sprites.add(invader)
                    enemy_group.add(invader)

    # Core State Processing Calculators Updates
    if not game_over:
        all_sprites.update()

        # Check for projectile impacts matching targeting groups
        hits = pygame.sprite.groupcollide(enemy_group, bullet_group, True, True)
        for hit in hits:
            score += 10
            new_invader = Enemy()
            all_sprites.add(new_invader)
            enemy_group.add(new_invader)

        # Monitor loss parameters conditions boundaries
        for invader in enemy_group:
            if invader.rect.bottom >= SCREEN_HEIGHT - 100:
                game_over = True

    # Draw active layers
    all_sprites.draw(screen)

    # UI Overlay Display Panel
    score_text = font.render(f"Score : {score}", True, (255, 255, 255))
    screen.blit(score_text, (20, 20))

    if game_over:
        over_text = game_over_font.render("GAME OVER", True, (255, 50, 50))
        sub_text = font.render("Press 'R' to Restart Game", True, (255, 255, 255))
        screen.blit(over_text, (SCREEN_WIDTH // 2 - 180, SCREEN_HEIGHT // 2 - 40))
        screen.blit(sub_text, (SCREEN_WIDTH // 2 - 180, SCREEN_HEIGHT // 2 + 40))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
