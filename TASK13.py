import pygame
import sys
pygame.init()
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Number Guessing Game - Moving Square")
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
square_size = 50
x = (WIDTH - square_size) // 2
y = (HEIGHT - square_size) // 2
speed = 5
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed
    if keys[pygame.K_RIGHT] and x < WIDTH - square_size:
        x += speed
    if keys[pygame.K_UP] and y > 0:
        y -= speed
    if keys[pygame.K_DOWN] and y < HEIGHT - square_size:
        y += speed
    screen.fill(BLACK)
    pygame.draw.rect(screen, BLUE, (x, y, square_size, square_size))
    pygame.display.flip()
pygame.quit()
sys.exit()
