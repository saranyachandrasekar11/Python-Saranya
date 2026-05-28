import pygame
import random

# Constants for easier adjustments
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400
MOVEMENT_SPEED = 5
FONT_SIZE = 72

# Initialize Pygame
pygame.init()

# Load and transform the background image
try:
    background_image = pygame.transform.scale(pygame.image.load("back1.jpg"),
                                              (SCREEN_WIDTH, SCREEN_HEIGHT))
    use_bg_image = True
except pygame.error:
    use_bg_image = False

# Load font once at the beginning
font = pygame.font.SysFont("Times New Roman", FONT_SIZE)


class Sprite(pygame.sprite.Sprite):

    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(pygame.Color('dodgerblue'))  # Background color of sprite
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
        self.rect = self.image.get_rect()

    def move(self, x_change, y_change, obstacles):
        # Move X safely
        self.rect.x += x_change
        self.rect.x = max(min(self.rect.x, SCREEN_WIDTH - self.rect.width), 0)
        for block in obstacles:
            if self.rect.colliderect(block.rect):
                if x_change > 0: self.rect.right = block.rect.left
                if x_change < 0: self.rect.left = block.rect.right

        # Move Y safely
        self.rect.y += y_change
        self.rect.y = max(min(self.rect.y, SCREEN_HEIGHT - self.rect.height), 0)
        for block in obstacles:
            if self.rect.colliderect(block.rect):
                if y_change > 0: self.rect.bottom = block.rect.top
                if y_change < 0: self.rect.top = block.rect.bottom


# Setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Collision with Obstacles")
all_sprites = pygame.sprite.Group()
obstacles_group = pygame.sprite.Group() # Group to hold the new obstacles

# Helper function to place sprites without overlapping instantly
def randomize_position(sprite):
    sprite.rect.x = random.randint(0, SCREEN_WIDTH - sprite.rect.width)
    sprite.rect.y = random.randint(0, SCREEN_HEIGHT - sprite.rect.height)

# Create Original Sprites
sprite1 = Sprite(pygame.Color('black'), 20, 30)
randomize_position(sprite1)
all_sprites.add(sprite1)
    
sprite2 = Sprite(pygame.Color('red'), 20, 30)
randomize_position(sprite2)
all_sprites.add(sprite2)

# ---- ADDED TWO NEW RECTANGULAR SPRITES ----
sprite3 = Sprite(pygame.Color('green'), 40, 40) # Green Obstacle
randomize_position(sprite3)
all_sprites.add(sprite3)
obstacles_group.add(sprite3)

sprite4 = Sprite(pygame.Color('yellow'), 50, 25) # Yellow Obstacle
randomize_position(sprite4)
all_sprites.add(sprite4)
obstacles_group.add(sprite4)
# --------------------------------------------

# Game loop control variables
running, won = True, False
clock = pygame.time.Clock()

# Main game loop
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN
                                         and event.key == pygame.K_x):
            running = False

    if not won:
        keys = pygame.key.get_pressed()
        x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * MOVEMENT_SPEED
        y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * MOVEMENT_SPEED
        
        # Pass the obstacle sprites to the move function to prevent walking through them
        sprite1.move(x_change, y_change, obstacles_group)

        # Win condition when touching the red target (sprite2)
        if sprite1.rect.colliderect(sprite2.rect):
            all_sprites.remove(sprite2)
            won = True

    # Drawing
    if use_bg_image:
        screen.blit(background_image, (0, 0))
    else:
        screen.fill(pygame.Color('lightgray')) # Fallback if image is missing
        
    all_sprites.draw(screen)

    # Display win message
    if won:
        win_text = font.render("You win!", True, pygame.Color('black'))
        screen.blit(win_text, ((SCREEN_WIDTH - win_text.get_width()) // 2,
                               (SCREEN_HEIGHT - win_text.get_height()) // 2))

    pygame.display.flip()
    clock.tick(90)

pygame.quit()
