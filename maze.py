################################
# Python Maze Generator
# First developed game
# RRR
# Angel Brandon Castillo Valdes
#################################
import pygame
import time
import random
# PG WINDOW SET UP
WIDTH = 800
HEIGHT = 800
FPS = 30

# Initialize PG
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption ("Grid")
clock = pygame.time.Clock()


# Define colours

WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
GREEN = [0, 255, 0]
YELLOW = [255, 255, 0]
BLUE = [0, 0, 255]
n=20
x=0
y= -WIDTH/n
grid = []
visited = []
stack = []
solution = {}
w= WIDTH/n

screen.fill(WHITE)
pygame.display.update()

# Build the grid
for i in range (0,n):
            x = w
            y = y + w
            for x in range (0,int(HEIGHT),int(w)):

                pygame.draw.line(screen, BLACK, [x, y], [x + WIDTH/n, y])                             # Top Cell
                pygame.draw.line(screen, BLACK, [x + WIDTH/n, y], [x + WIDTH/n, y + WIDTH/n])         # right cell
                pygame.draw.line(screen, BLACK, [x + WIDTH/n, y + WIDTH/n], [x, y + WIDTH/n])         # bottom cell
                pygame.draw.line(screen, BLACK, [x, y + WIDTH/n], [x, y])                             # left cell
                grid.append((x, y))                                                 # add cell to grid list
                pygame.display.update()
                x = x + w


pygame.display.update()


### PG LOOP ####
running = True
while running:
    # keep running at the right speed
    clock.tick(FPS)
    # process input (events)
    for event in pygame.event.get():
        # check whether the window gets closed
        if event.type == pygame.QUIT:
            running= False