import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bullet Echo Lite")

# Player
x, y = 400, 300
speed = 5

clock = pygame.time.Clock()

# Light surface
light_surface = pygame.Surface((WIDTH, HEIGHT))
light_surface.set_alpha(200)  # darkness level

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    # Draw background
    screen.fill((50, 50, 50))

    # Player
    pygame.draw.circle(screen, (0, 255, 0), (x, y), 10)

    # Darkness
    light_surface.fill((0, 0, 0))

    # Light circle
    pygame.draw.circle(light_surface, (255, 255, 255), (x, y), 120)

    # Blend
    screen.blit(light_surface, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)

    pygame.display.flip()
    clock.tick(60)