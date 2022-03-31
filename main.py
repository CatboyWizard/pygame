#Imports
import pygame
from pygame import platform

#Import from pygame.locals
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

def ground(lvl,x,y,w,h):
    ground_list = pygame.sprite.Group()
    if lvl == 1:
        ground = Platform(x,y,w,h,'block-ground.png')
        ground_list.add(ground)

    if lvl == 2:
        print("Level " + str(lvl) )

    return ground_list

def platform( lvl ):
    plat_list = pygame.sprite.Group()
    if lvl == 1:
        plat = Platform(200, worldy-97-128, 285,67,'block-big.png')
        plat_list.add(plat)
        plat = Platform(500, worldy-97-320, 197,54,'block-small.png')
        plat_list.add(plat)
    if lvl == 2:
        print("Level " + str(lvl) )
       
    return plat_list