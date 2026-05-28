import pygame
import random
import math
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Setup Window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invader")
clock = pygame.time.Clock()

# Fonts
font = pygame.font.SysFont("Arial", 36, bold=True)
game_over_font = pygame.font.SysFont("Arial", 64, bold=True)

# ---------------------------------------------------------
# PROCEDURAL GRAPHICS GENERATORS
# ---------------------------------------------------------
def create_player_surf():
    surf = pygame.Surface((60, 60), pygame.SRCALPHA)
    # Side Boosters
    pygame.draw.rect(surf, (0, 191, 255), (10, 35, 8, 20), border_radius=3)
    pygame.draw.rect(surf, (0, 191, 255), (42, 35, 8, 20), border_radius=3)
    # Main Body
    pygame.draw.ellipse(surf, (240, 240, 240), (20, 5, 20, 50))
    # Nose Cone
    pygame.draw.polygon(surf, (255, 69, 0), [(20, 20), (30, 0), (40, 20)])
    # Wings
    pygame.draw.polygon(surf, (255, 69, 0), [(20, 35), (5, 45), (20, 45)])
    pygame.draw.polygon(surf, (255, 69, 0), [(40, 35), (55, 45), (40, 45)])
    return surf

def create_enemy_surf():
    surf = pygame.Surface((50, 40), pygame.SRCALPHA)
    # Retro Alien Shape (Pixel style representation)
    body_color = (255, 69, 0) # Vibrant Orange-Red like image
    pygame.draw.ellipse(surf, body_color, (5, 5, 40, 30))
    # Eyes
    pygame.draw.circle(surf, (30, 30, 30), (18, 18), 4)
    pygame.draw.circle(surf, (30, 30, 30), (32, 18), 4)
    # Antennae / Legs
    pygame.draw.line(surf, body_color, (15, 5), (10, 0), 3)
    pygame.draw.line(surf, body_color, (35, 5), (40, 0), 3)
    pygame.draw.line(surf, body_color, (12, 32), (8, 38), 3)
    pygame.draw.line(surf, body_color, (38, 32), (42, 38), 3)
    pygame.draw.line(surf, body_color, (25, 33), (25, 39), 3)
    return surf

# Generate Asset Surfaces
player_image = create_player_surf()
enemy_image = create_enemy_surf()

# ---------------------------------------------------------
# BACKGROUND SCENE SETUP (Stars, Planets, Meteors)
# ---------------------------------------------------------
stars = [(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)) for _ in range(120)]
meteors = [
    {"pos": [250, 100], "size": 30},
    {"pos": [150, 450], "size": 20},
    {"pos": [600, 50], "size": 25}
]

# ---------------------------------------------------------
# GAME ENTITIES CLASSES
# ---------------------------------------------------------
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 60))
        self.speed = 6

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
        # Clamp bounds
        self.rect.left = max(0, self.rect.left)
        self.rect.right = min(SCREEN_WIDTH, self.rect.right)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_image
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
        self.image = pygame.Surface((6, 18))
        self.image.fill((255, 255, 0)) # Yellow lasers
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 10

    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()

# Manage Sprite Groups
all_sprites = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

# Create initial swarm (Matching the image's setup layout)
for i in range(5):
    invader = Enemy()
    all_sprites.add(invader)
    enemy_group.add(invader)

# Game Rules Initialization
score = 0
game_over = False

# ---------------------------------------------------------
# MAIN CORE GAME LOOP
# ---------------------------------------------------------
running = True
while running:
    # 1. Background Render Layer (Deep Space Layout)
    screen.fill((12, 19, 56)) # Dark Nebula Navy Blue Base
    
    # Render Starfield background
    for star in stars:
        pygame.draw.circle(screen, (255, 255, 255), star, 1)

    # Render Moon & Background Planets
    pygame.draw.circle(screen, (160, 160, 170), (740, 140), 65) # Top Right Moon
    pygame.draw.circle(screen, (140, 140, 150), (700, 110), 10) # Moon Crater
    pygame.draw.circle(screen, (0, 206, 209), (430, 100), 28)  # Teal Planet Center Top
    pygame.draw.circle(screen, (220, 80, 30), (30, 320), 25)   # Orange Planet Left Edge

    # Render Diagonal Meteors Streaking
    for m in meteors:
        p = m["pos"]
        pygame.draw.line(screen, (255, 140, 0), (p[0], p[1]), (p[0] + m["size"], p[1] - m["size"]), 4)
        pygame.draw.circle(screen, (255, 69, 0), (p[0], p[1]), 3)

    # 2. Input Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                # Limit fire rate natively (max 2 lasers on screen)
                if len(bullet_group) < 2:
                    laser = Bullet(player.rect.centerx, player.rect.top)
                    all_sprites.add(laser)
                    bullet_group.add(laser)
            elif event.key == pygame.K_r and game_over: # Restart Option
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

    # 3. Game Logic Updates
    if not game_over:
        all_sprites.update()

        # Laser vs Invader Collision Handler
        hits = pygame.sprite.groupcollide(enemy_group, bullet_group, True, True)
        for hit in hits:
            score += 10
            # Instantly respawn new ones to keep action constant
            new_invader = Enemy()
            all_sprites.add(new_invader)
            enemy_group.add(new_invader)

        # Game Over Check (If invaders pass safety thresholds or reach player)
        for invader in enemy_group:
            if invader.rect.bottom >= SCREEN_HEIGHT - 100:
                game_over = True

    # 4. Entity Draw Layer
    all_sprites.draw(screen)

    # UI Heads Up Display
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
