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
pygame.display.set_caption("Custom Event: Color Changing Sprites")
clock = pygame.time.Clock()

# --- CUSTOM EVENT DEFINITION ---
# Pygame custom events must use IDs between pygame.USEREVENT and pygame.NUMEVENTS
CHANGE_COLOR_EVENT = pygame.USEREVENT + 1

# Trigger the custom event every 1500 milliseconds (1.5 seconds)
pygame.time.set_timer(CHANGE_COLOR_EVENT, 1500)


class ColorSprite(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.image = pygame.Surface([width, height])
        
        # Give it an initial random color
        self.change_color()
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def change_color(self):
        """Generates a random RGB color and applies it to the sprite surface."""
        random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.image.fill(random_color)


# Create two separate sprite instances
sprite1 = ColorSprite(x=200, y=200, width=120, height=120)
sprite2 = ColorSprite(x=480, y=200, width=120, height=120)

# Add them to the sprite tracking group
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
            
        # --- LISTEN FOR THE CUSTOM EVENT ---
        elif event.type == CHANGE_COLOR_EVENT:
            sprite1.change_color()
            sprite2.change_color()

    # Drawing Environment
    screen.fill((30, 30, 30))  # Dark gray background
    all_sprites.draw(screen)   # Draw both sprites to the screen
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
