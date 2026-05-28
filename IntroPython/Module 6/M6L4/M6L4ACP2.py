import pygame
import random

# Constants for easier adjustments
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400
MOVEMENT_SPEED = 5
FONT_SIZE = 72
SUB_FONT_SIZE = 36

# Initialize Pygame
pygame.init()

# Load and transform the background image
try:
    background_image = pygame.transform.scale(pygame.image.load("back1.jpg"),
                                              (SCREEN_WIDTH, SCREEN_HEIGHT))
    use_bg_image = True
except pygame.error:
    use_bg_image = False

# Load fonts once at the beginning
font = pygame.font.SysFont("Times New Roman", FONT_SIZE)
sub_font = pygame.font.SysFont("Times New Roman", SUB_FONT_SIZE)


class Sprite(pygame.sprite.Sprite):

    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(pygame.Color('dodgerblue'))  # Background color of sprite
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
        self.rect = self.image.get_rect()

    def move(self, x_change, y_change):
        # Boundary-restricted movement
        self.rect.x = max(min(self.rect.x + x_change, SCREEN_WIDTH - self.rect.width), 0)
        self.rect.y = max(min(self.rect.y + y_change, SCREEN_HEIGHT - self.rect.height), 0)


# Setup Screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Collision - Avoid Obstacles!")
clock = pygame.time.Clock()

# Sprite References
sprite1 = None
sprite2 = None
sprite3 = None
sprite4 = None
all_sprites = pygame.sprite.Group()
obstacles_group = pygame.sprite.Group()

def randomize_position(sprite):
    sprite.rect.x = random.randint(0, SCREEN_WIDTH - sprite.rect.width)
    sprite.rect.y = random.randint(0, SCREEN_HEIGHT - sprite.rect.height)

def reset_game():
    """Resets the entire game state and relocates sprites."""
    global sprite1, sprite2, sprite3, sprite4, game_state
    
    all_sprites.empty()
    obstacles_group.empty()
    
    # Player
    sprite1 = Sprite(pygame.Color('black'), 20, 30)
    randomize_position(sprite1)
    all_sprites.add(sprite1)
        
    # Target (Win Condition)
    sprite2 = Sprite(pygame.Color('red'), 20, 30)
    randomize_position(sprite2)
    all_sprites.add(sprite2)

    # Harmful Obstacle 1
    sprite3 = Sprite(pygame.Color('green'), 40, 40)
    randomize_position(sprite3)
    all_sprites.add(sprite3)
    obstacles_group.add(sprite3)

    # Harmful Obstacle 2
    sprite4 = Sprite(pygame.Color('yellow'), 50, 25)
    randomize_position(sprite4)
    all_sprites.add(sprite4)
    obstacles_group.add(sprite4)
    
    # States: 'PLAYING', 'WON', 'GAMEOVER'
    game_state = 'PLAYING'

# Initialize the first game state
reset_game()
running = True

# Main game loop
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN
                                         and event.key == pygame.K_x):
            running = False
        
        # Press 'R' to restart when game is over or won
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            if game_state != 'PLAYING':
                reset_game()

    # Core Logic
    if game_state == 'PLAYING':
        keys = pygame.key.get_pressed()
        x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * MOVEMENT_SPEED
        y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * MOVEMENT_SPEED
        sprite1.move(x_change, y_change)

        # LOSE condition: Player touches green or yellow obstacles
        if pygame.sprite.spritecollideany(sprite1, obstacles_group):
            game_state = 'GAMEOVER'

        # WIN condition: Player touches the red target
        elif sprite1.rect.colliderect(sprite2.rect):
            all_sprites.remove(sprite2)
            game_state = 'WON'

    # Drawing
    if use_bg_image:
        screen.blit(background_image, (0, 0))
    else:
        screen.fill(pygame.Color('lightgray'))
        
    all_sprites.draw(screen)

    # Display Overlay Screens
    if game_state == 'WON':
        text = font.render("You Win!", True, pygame.Color('black'))
        sub_text = sub_font.render("Press 'R' to Play Again", True, pygame.Color('blue'))
        screen.blit(text, ((SCREEN_WIDTH - text.get_width()) // 2, (SCREEN_HEIGHT - text.get_height()) // 2 - 20))
        screen.blit(sub_text, ((SCREEN_WIDTH - sub_text.get_width()) // 2, (SCREEN_HEIGHT - sub_text.get_height()) // 2 + 50))

    elif game_state == 'GAMEOVER':
        text = font.render("Game Over!", True, pygame.Color('crimson'))
        sub_text = sub_font.render("Press 'R' to Try Again", True, pygame.Color('black'))
        screen.blit(text, ((SCREEN_WIDTH - text.get_width()) // 2, (SCREEN_HEIGHT - text.get_height()) // 2 - 20))
        screen.blit(sub_text, ((SCREEN_WIDTH - sub_text.get_width()) // 2, (SCREEN_HEIGHT - sub_text.get_height()) // 2 + 50))

    pygame.display.flip()
    clock.tick(90)

pygame.quit()
