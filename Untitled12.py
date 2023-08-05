#!/usr/bin/env python
# coding: utf-8

# # PACMAN GAME Python Model

# In[3]:


import pygame
import random

pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
CELL_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // CELL_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // CELL_SIZE
PACMAN_SPEED = 3
GHOST_SPEED = 2
PACMAN_COLOR = (255, 255, 0)
GHOST_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
FOOD_COLOR = (255, 255, 255)

class Pacman:
    def __init__(self):
        self.x, self.y = GRID_WIDTH // 2, GRID_HEIGHT // 2
        self.direction = (0, 0)
        self.score = 0

    def move(self):
        dx, dy = self.direction
        new_x, new_y = self.x + dx, self.y + dy

        # Check for collisions with walls
        if not 0 <= new_x < GRID_WIDTH or not 0 <= new_y < GRID_HEIGHT:
            return

        # Check for collisions with ghosts
        for ghost in ghosts:
            if ghost.x == new_x and ghost.y == new_y:
                return

        self.x, self.y = new_x, new_y

        # Check for collisions with food
        if (self.x, self.y) in food:
            self.score += 10
            food.remove((self.x, self.y))

class Ghost:
    def __init__(self, color):
        self.x, self.y = random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)
        self.color = color

    def move(self):
        dx, dy = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
        new_x, new_y = self.x + dx, self.y + dy

        # Check for collisions with walls and other ghosts
        if not 0 <= new_x < GRID_WIDTH or not 0 <= new_y < GRID_HEIGHT:
            return

        for ghost in ghosts:
            if ghost.x == new_x and ghost.y == new_y:
                return

        self.x, self.y = new_x, new_y

# Helper function
def draw_grid(surface):
    for x in range(0, SCREEN_WIDTH, CELL_SIZE):
        pygame.draw.line(surface, (100, 100, 100), (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, CELL_SIZE):
        pygame.draw.line(surface, (100, 100, 100), (0, y), (SCREEN_WIDTH, y))

# Initialize Pacman and Ghosts
pacman = Pacman()
ghosts = [Ghost(color) for color in GHOST_COLORS]

# Generate random food positions
food = [(random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)) for _ in range(20)]

# Main game loop
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pacman Game")
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    pacman.direction = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT], keys[pygame.K_DOWN] - keys[pygame.K_UP])

    pacman.move()
    for ghost in ghosts:
        ghost.move()

    # Check for collisions with ghosts
    for ghost in ghosts:
        if ghost.x == pacman.x and ghost.y == pacman.y:
            print("Game Over! Your Score:", pacman.score)
            running = False

    screen.fill((0, 0, 0))
    draw_grid(screen)

    # Draw Pacman, Ghosts, and Food
    pygame.draw.circle(screen, PACMAN_COLOR, (pacman.x * CELL_SIZE + CELL_SIZE // 2, pacman.y * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2)
    for ghost in ghosts:
        pygame.draw.circle(screen, ghost.color, (ghost.x * CELL_SIZE + CELL_SIZE // 2, ghost.y * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2)
    for f in food:
        pygame.draw.rect(screen, FOOD_COLOR, (f[0] * CELL_SIZE, f[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()


# In[ ]:




