import pygame
import sys

# 1. Initialize Pygame
pygame.init()

# 2. Set up the screen dimensions (Width, Height)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 3. Set the window title
pygame.display.set_caption("My First Game Screen")

# Define colors (RGB format)
BACKGROUND_COLOR = (50, 150, 255)  # A nice sky blue

# 4. Main Game Loop
running = True
while running:
    # Look for events (like clicking the X button)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with the background color
    screen.fill(BACKGROUND_COLOR)

    # Update the display to show the changes
    pygame.display.flip()

# 5. Clean up and exit
pygame.quit()
sys.exit()
