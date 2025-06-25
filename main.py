import pygame
import math
from random import randrange, uniform
from pygame.math import Vector2
import config

pygame.init()
pygame.mixer.init()

try:
    pygame.mixer.music.load("audio/chime.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
    feedback_sound = pygame.mixer.Sound("audio/shatter2.mp3")
except FileNotFoundError:
    print("Audio file not found. Running without sound.")
    feedback_sound = None
    

# Set up the display
screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
pygame.display.set_caption("Shatter - Visual Effects")
pygame.mouse.set_cursor(pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_CROSSHAIR))
clock = pygame.time.Clock()
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
        self.age += dt
        if self.age >= self.lifespan:
            self.alive = False
            return
        
     # Reduce speed over time
        current_speed = self.speed * (1 - self.age / self.lifespan)
        self.loc.x += math.cos(self.angle) * current_speed * dt
        self.loc.y += math.sin(self.angle) * current_speed * dt

        # Update alpha for fading
        self.alpha = int(255 * (1 - self.age / self.lifespan))
        self.color = (self.color[0], self.color[1], self.color[2], self.alpha)
    
    def draw(self, surf, offset=[0, 0]):
        if self.alive and self.alpha > 0:
            points = [
                [self.loc.x + offset[0], self.loc.y + offset[1]],  # Center
                [self.loc.x + math.cos(self.angle) * self.speed * self.scale + offset[0],
                self.loc.y + math.sin(self.angle) * self.speed * self.scale + offset[1]],  # Forward tip
                [self.loc.x + math.cos(self.angle + math.pi / 2) * self.speed * self.scale * 0.3 + offset[0],
                self.loc.y + math.sin(self.angle + math.pi / 2) * self.speed * self.scale * 0.3 + offset[1]],  # Right wing
                [self.loc.x + math.cos(self.angle - math.pi / 2) * self.speed * self.scale * 0.3 + offset[0],
                self.loc.y + math.sin(self.angle - math.pi / 2) * self.speed * self.scale * 0.3 + offset[1]],  # Left wing
            ]
            surface_size = int(self.scale * 20)
            spark_surface = pygame.Surface((surface_size, surface_size), pygame.SRCALPHA)
            pygame.draw.polygon(spark_surface, (*self.color[:3], self.alpha), [(p[0] - self.loc.x, p[1] - self.loc.y) for p in points])
            surf.blit(spark_surface, (self.loc.x - surface_size / 2, self.loc.y - surface_size / 2))
            
    def update(self, dt):
        self.move(dt)


shards = []
executing = True
duration = 0

# Main loop
while executing:
    dt = clock.tick(config.FPS) / 1000
    duration += dt
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            print(f"➡️ quit by closing the application window")
            executing = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
            config.BG_COLOR = (randrange(0, 40), randrange(0, 40), randrange(0, 40))
            print(f"➡️ background color changed to rgb{config.BG_COLOR}")
        if event.type == pygame.MOUSEBUTTONDOWN:
            feedback_sound.play()
            mx, my = pygame.mouse.get_pos()
            print(f"➡️ clicked at {mx, my}")
            for _ in range(40):
                angle = math.radians(randrange(0, 360))
                speed = randrange(100, 300)
                scale = uniform(0.5, 1.5)
                color = (config.SHARD_COLOR)
                shards.append(Shard(mx, my, angle, speed, color, scale))
    
    screen.fill(config.BG_COLOR) 
    to_remove = []  # Collect indices of shards to remove
    for i, shard in enumerate(shards[::-1]):  # Reverse order for drawing
        shard.update(dt)
        shard.draw(screen)
        if not shard.alive:
            to_remove.append(len(shards) - 1 - i)  # Store original index
    for index in sorted(to_remove, reverse=True):  # Remove from highest to lowest index
        shards.pop(index)
    pygame.display.flip()

pygame.quit()
print(f"Execution loop was running for {round(duration, 2)}s.")
          
