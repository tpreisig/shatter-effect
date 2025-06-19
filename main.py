import pygame
import math
from random import randrange, uniform
from pygame.math import Vector2
import config

pygame.init()


# Set up the display
screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
pygame.display.set_caption("Shatter - Visual Effects")
pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_CROSSHAIR))
clock = pygame.time.Clock()
screen.fill((0, 0, 64))
class Shard:
    def __init__(self, x, y, angle, speed, color, scale, lifespan=4.0):
        self.loc = Vector2(x, y)
        self.angle = angle
        self.speed = speed
        self.color = color
        self.scale = scale
        self.lifespan = lifespan
        self.age = 0.0
        self.alive = True
        self.alpha = int(255 *  (1 - 2 * self.age / self.lifespan))
        
    def move(self, dt):
        pass
    
    def draw(self, surf):
        pass
        
    def update(self, dt):
        self.move(dt)


shards = []
executing = True
duration = 0

while executing:
    dt = clock.tick(config.FPS)/1000
    duration += dt
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            print(f"➡️ quit by closing the application window")
            executing = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
            bg_color = (randrange(0, 100), randrange(0, 100), randrange(0, 100))
            print(f"➡️ background color changed to rgb{bg_color}")
            screen.fill(bg_color)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            print(f"➡️ clicked at {mx, my}")
            for _ in range(40):
                angle = math.radians(randrange(0, 360))
                speed = randrange(100, 300)
                scale = uniform(0.5, 1.5)
                color = (255, 25, 255)
                shards.append(Shard(mx, my, angle, speed, color, scale))
    for i, shard in sorted(enumerate(shards), reverse=True):
        shard.update(dt)
        shard.draw(screen)
        if not shard.alive:
            shard.pop(i)
    pygame.display.flip()
pygame.quit()
print(f"Execution loop was running for {round(duration, 2)}s.")
          
