#Imports
from cProfile import run
from json import load
from re import X
import sys
from webbrowser import BackgroundBrowser
import pygame
from turtle import Screen, width

#Import pygame.locals for easier access to key coordinates
#Updated to conform to flake8 and black standards
from pygame.locals import(
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    MOUSEBUTTONDOWN,
    MOUSEBUTTONUP,
    K_SPACE,
    )

#Initialize pygame
pygame.init()

#Define constants fpr the screen width and height
WIDTH = 800
Height = 400
fps = 60
clock =pygame.time.Clock()

#display/mosue
display = pygame.display.set_mode((WIDTH, Height))

pygame.mouse.set_visible(0)

Background = BackgroundBrowser

ground = (900, 120, -20, 320, "white-background-2.png")

player = (200,200)

Group1 = pygame.sprite.Group()
Group1.add(ground)

# !main code
while True:

    for event in pygame.event.get():
        
        if event.type == QUIT:
            pygame.quit()

        if event.type == MOUSEBUTTONDOWN:
            pass
        
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                player.jump()

    player.update(Group1)

    display.blite(Background, (0,0))
    ground.render(display)
    player.render(display)

    pygame.display.update()
    clock.tick(fps)