import pygame
import sys
import random

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Initialize Pygame
pygame.init()

# Setup Screen and Clock
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Custom Events: Independent Color & Size Shifting")
clock = pygame.time.Clock()

# --- DEFINE TWO UNIQUE CUSTOM EVENTS ---
# Each custom event needs its own unique numeric ID slot
SPRITE1_EVENT = pygame.USEREVENT + 1
SPRITE2_EVENT = pygame.USEREVENT + 2

# Set different timer intervals (Sprite 1 changes faster than Sprite 2)
pygame.time.set_timer(SPRITE1_EVENT, 800)   # Every 0.8 seconds
pygame.time.set_timer(SPRITE2_EVENT, 1600)  # Every 1.6 seconds


class AdvancedSprite(pygame.sprite.Sprite):

    def __init__(self, center_x, center_y):
        super().__init__()
        self.center_x = center_x
        self.center_y = center_y
        
        # Call the modification method to establish initial color and size
        self.mutate_sprite()

    def mutate_sprite(self):
        """Changes both the sprite's color and dimensions simultaneously."""
        # 1. Generate a new random size variant
        new_width = random.randint(60, 160)
        new_height = random.randint(60, 160)
        
        # 2. Recreate the surface canvas with the new sizes
        self.image = pygame.Surface([new_width, new_height])
        
        # 3. Generate and fill with a random color
        random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.image.fill(random_color)
        
        # 4. Re-anchor the rect bounding box around the original center point
        self.rect = self.image.get_rect()
        self.rect.center = (self.center_x, self.center_y)


# Create two separate sprite instances anchored to their screen center-points
sprite1 = AdvancedSprite(center_x=250, center_y=300)
sprite2 = AdvancedSprite(center_x=550, center_y=300)

# Add them to the tracking group
all_sprites = pygame.sprite.Group()
all_sprites.add(sprite1)
all_sprites.add(sprite2)

# Main Game Loop
running = True
while running:
    # Event Handling Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        # --- LISTEN FOR INDEPENDENT CUSTOM EVENTS ---
        elif event.type == SPRITE1_EVENT:
            sprite1.mutate_sprite()
            
        elif event.type == SPRITE2_EVENT:
            sprite2.mutate_sprite()

    # Drawing Environment
    screen.fill((25, 25, 35))  # Dark midnight blue background
    all_sprites.draw(screen)   # Draw both mutating sprites
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
