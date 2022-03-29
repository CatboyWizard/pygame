from operator import truediv
from webbrowser import get
import pygame
pygame.init()

screen = pygame.display.set_mode([500, 500])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
screen.fill((225, 225, 225))

pygame.draw.circle(screen, (0, 0, 225), (250, 250), 75)

pygame.display.flip()

pygame.quit()