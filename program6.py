#Develop a program to demonstrate Animation effects on simple objects.
import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Animation Effects")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Number of objects
num_objects = 10
colors = [RED, GREEN, BLUE]

# Object list
objects = []
for _ in range(num_objects):
    x = random.randint(50, screen_width - 50)
    y = random.randint(50, screen_height - 50)
    radius = random.randint(10, 20)  # Ensure positive radius
    speedx = random.randint(-5, 5)
    speedy = random.randint(-5, 5)
    color = random.choice(colors)
    objects.append({"x": x, "y": y, "radius": radius, "color": color, "speedx": speedx, "speedy": speedy})

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    for obj in objects:
        # Update object position
        obj["x"] += obj["speedx"]
        obj["y"] += obj["speedy"]

        # Check for collision with screen boundaries
        if obj["x"] - obj["radius"] < 0 or obj["x"] + obj["radius"] > screen_width:
            obj["speedx"] = -obj["speedx"]
        if obj["y"] - obj["radius"] < 0 or obj["y"] + obj["radius"] > screen_height:
            obj["speedy"] = -obj["speedy"]

        # Draw the object
        pygame.draw.circle(screen, obj["color"], (obj["x"], obj["y"]), obj["radius"])

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
