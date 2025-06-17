import pygame
import math
import random
from pygame.math import Vector2

pygame.init()

# Configuration
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Shatter - Visual Effects")
clock = pygame.time.Clock()

shatter = []
executing = True

while executing:
    dt = clock.tick(FPS)/1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            executing = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
            pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_CROSSHAIR))
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            print(f"cursor at {mx, my}")
    screen.fill((200, 230, 250))
    pygame.display.flip()
pygame.quit()
          
