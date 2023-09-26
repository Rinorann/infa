import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

circle(screen, (255, 255, 0), (200, 175), 100)
circle(screen, (255, 1, 1), (150, 150), 25)
circle(screen, (255, 1, 1), (250, 160), 15)
circle(screen, (0, 0, 0), (150, 150), 15)
circle(screen, (0, 0, 0), (250, 160), 7)
rect(screen, (1, 1, 1), (150, 225, 100, 14))
polygon(screen, (0, 0, 0), [(100,100), (120, 90), (210, 120), (200, 150)])
polygon(screen, (0, 0, 0), [(300,100), (320, 90), (225, 120), (225, 150)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()