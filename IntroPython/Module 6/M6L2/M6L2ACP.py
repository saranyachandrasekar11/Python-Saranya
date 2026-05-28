import pygame
import sys

# 1. Initialize Pygame and the Font system
pygame.init()
pygame.font.init()

# 2. Set up the screen dimensions and title
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Shapes and Text in Pygame")

# 3. Define Colors (RGB format)
DARK_GRAY = (30, 30, 30)
NEON_GREEN = (57, 255, 20)
WHITE = (255, 255, 255)

# 4. Set up the Font object (System default font, size 36)
game_font = pygame.font.SysFont("Arial", 36)

# Render the text surface (Text, Anti-aliasing, Color)
text_surface = game_font.render("Welcome to Pygame!", True, WHITE)

# 5. Main Game Loop
running = True
while running:
    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen with a background color
    screen.fill(DARK_GRAY)

    # 6. Draw a Rectangle
    # Arguments: (Surface to draw on, Color, [X_Position, Y_Position, Width, Height])
    pygame.draw.rect(screen, NEON_GREEN, [100, 150, 200, 100])

    # 7. Draw the Text
    # Arguments: (Text Surface, [X_Position, Y_Position])
    screen.blit(text_surface, (100, 300))

    # Update the display
    pygame.display.flip()

# Clean up and exit
pygame.quit()
sys.exit()
