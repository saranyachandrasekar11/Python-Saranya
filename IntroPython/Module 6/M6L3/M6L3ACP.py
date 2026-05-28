import pygame
import random

# Initialize pygame-ce
pygame.init()

# Setup game window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Colorful Bounce - Two Squares")

def get_random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Global background color
bg_color = get_random_color()

# Square definition class to manage multiple objects easily
class BouncingSquare:
    def __init__(self, size, x, y, speed_x, speed_y):
        self.size = size
        self.x = x
        self.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.color = get_random_color()

    def update_and_bounce(self):
        global bg_color
        # Move
        self.x += self.speed_x
        self.y += self.speed_y
        bounced = False

        # Left/Right wall collision
        if self.x <= 0 or self.x + self.size >= WIDTH:
            self.speed_x *= -1
            bounced = True

        # Top/Bottom wall collision
        if self.y <= 0 or self.y + self.size >= HEIGHT:
            self.speed_y *= -1
            bounced = True

        # Update colors on bounce
        if bounced:
            self.color = get_random_color()
            bg_color = get_random_color()

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.size, self.size))

# Create two squares with distinct sizes, positions, and speeds
square1 = BouncingSquare(size=60, x=100, y=100, speed_x=5, speed_y=4)
square2 = BouncingSquare(size=50, x=600, y=400, speed_x=-4, speed_y=6)

clock = pygame.time.Clock()
running = True

# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update logic
    square1.update_and_bounce()
    square2.update_and_bounce()

    # Drawing logic
    screen.fill(bg_color)
    square1.draw(screen)
    square2.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
