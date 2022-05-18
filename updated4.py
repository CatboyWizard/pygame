from cgitb import text
from time import sleep
import pygame
import sys
import os
import math
import random
from pygame.locals import *
from pygame import mixer
from pygame.image import load as getImage
pygame.init()

'''
Variables
'''

Screen = pygame.display.set_mode((1000, 680))
dir_img = 'C:\\Users\\mchugh_kevin\\Desktop\\pygame\\images\\'
ani = 6
pygame.display.set_caption("Game")

BLUE = (25, 25, 200)
BLACK = (23, 23, 23)
WHITE = (254, 254, 254)
ALPHA = (0, 255, 0)
RED = (255,0,0)

clock = pygame.time.Clock()

mixer.init()
mixer.music.load('C:\\Users\\mchugh_kevin\\Desktop\\pygame\\images\\sounds\\Lofi Hip Hop.mp3')
mixer.music.play()
mixer.music.set_volume(0.05)

'''
Objects
'''

class Human(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
    
    def left(self,x,y):
        global walkCount
        Screen.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1

    def right(self,x,y):
        global walkCount
        Screen.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1


human = Human()

class Platform(pygame.sprite.Sprite):
    def __init__(self, xloc, yloc, imgw, imgh, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = getImage(os.path.join('images', img)).convert()
        self.image.convert_alpha()
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()
        self.rect.y = yloc
        self.rect.x = xloc

class Enemy(pygame.sprite.Sprite):

    def __init__(self, x, y, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('images', img))
        self.image.convert_alpha()
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.counter = 0

    def left(self,x,y):
        global walkCount
        Screen.blit(walkLeft2[walkCount//3], (x,y))
        walkCount += 1

    def right(self,x,y):
        global walkCount
        Screen.blit(walkRight2[walkCount//3], (x,y))
        walkCount += 1

enemy = Enemy

'''
Walking
'''

walkRight = [getImage(dir_img+'R1.png'), getImage(dir_img+'R2.png'), getImage(dir_img+'R3.png'), getImage(dir_img+'R4.png'), getImage(dir_img+'R5.png'), getImage(dir_img+'R6.png'), getImage(dir_img+'R7.png'), getImage(dir_img+'R8.png'), getImage(dir_img+'R9.png')]
walkLeft = [getImage(dir_img+'L1.png'), getImage(dir_img+'L2.png'), getImage(dir_img+'L3.png'), getImage(dir_img+'L4.png'), getImage(dir_img+'L5.png'), getImage(dir_img+'L6.png'), getImage(dir_img+'L7.png'), getImage(dir_img+'L8.png'), getImage(dir_img+'L9.png')]
bg = getImage(dir_img+'drawing3.jpg')
char = getImage(dir_img+'standing.png')

walkRight2 = [getImage(dir_img+'R1E.png'), getImage(dir_img+'R2E.png'), getImage(dir_img+'R3E.png'), getImage(dir_img+'R4E.png'), getImage(dir_img+'R5E.png'), getImage(dir_img+'R6E.png'), getImage(dir_img+'R7E.png'), getImage(dir_img+'R8E.png'), getImage(dir_img+'R9E.png'), getImage(dir_img+'R10E.png'), getImage(dir_img+'R11E.png')]
walkLeft2 =  [getImage(dir_img+'L1E.png'), getImage(dir_img+'L2E.png'), getImage(dir_img+'L3E.png'), getImage(dir_img+'L4E.png'), getImage(dir_img+'L5E.png'), getImage(dir_img+'L6E.png'), getImage(dir_img+'L7E.png'), getImage(dir_img+'L8E.png'), getImage(dir_img+'L9E.png'), getImage(dir_img+'L10E.png'), getImage(dir_img+'L11E.png')]

x = 500
y = 500
width = 60
height = 60
vel = 5

isJump = False
jumpCount = 10

left = False
right = False
walkCount = 0

def redrawGameWindow():
    global walkCount
    
    Screen.blit(bg, (0,0))  
    if walkCount + 1 >= 27:
        walkCount = 0
        
    if left:           
        human.left(x,y)           
    elif right:
        human.right(x,y)
    else:
        Screen.blit(char, (x, y))
        walkCount = 0
        
    pygame.display.update()

run = True

while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a] and x > vel: 
        x -= vel
        left = True
        right = False

    elif keys[pygame.K_d] and x < 500 - vel - width:  
        x += vel
        left = False
        right = True
    
    else: 
        left = False
        right = False
        walkCount = 0
        
    if not(isJump):
        if keys[pygame.K_w]:
            isJump = True
            left = False
            right = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else: 
            jumpCount = 10
            isJump = False

    redrawGameWindow() 

pygame.quit()