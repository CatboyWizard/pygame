from cgitb import text
from distutils.file_util import move_file
from shutil import move
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

walkRight = [getImage(dir_img+'R1.png'), getImage(dir_img+'R2.png'), getImage(dir_img+'R3.png'), getImage(dir_img+'R4.png'), getImage(dir_img+'R5.png'), getImage(dir_img+'R6.png'), getImage(dir_img+'R7.png'), getImage(dir_img+'R8.png'), getImage(dir_img+'R9.png')]
walkLeft = [getImage(dir_img+'L1.png'), getImage(dir_img+'L2.png'), getImage(dir_img+'L3.png'), getImage(dir_img+'L4.png'), getImage(dir_img+'L5.png'), getImage(dir_img+'L6.png'), getImage(dir_img+'L7.png'), getImage(dir_img+'L8.png'), getImage(dir_img+'L9.png')]
bg = getImage(dir_img+'drawing3.jpg')
char = getImage(dir_img+'standing.png')

clock = pygame.time.Clock()

hitSound = pygame.mixer.Sound('C:\\Users\\mchugh_kevin\\Desktop\\pygame\\images\\sounds\\Game_hit.mp3')

score = 0

class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        #pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    def hit(self):
        self.isJump = False
        self.jumpCount = 10
        self.x -= 100
        self.walkCount = 0
        font1 = pygame.font.SysFont('comicsans', 100)
        text = font1.render('-5', 1, (255,0,0))
        Screen.blit(text, (250 - (text.get_width()/2),200))
        pygame.display.update()
        i = 0
        while i < 200:
            pygame.time.delay(10)
            i += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = 201
                    pygame.quit()
                
class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self,win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius)

class enemy(object):
    walkRight = [getImage(dir_img+'R1E.png'), getImage(dir_img+'R2E.png'), getImage(dir_img+'R3E.png'), getImage(dir_img+'R4E.png'), getImage(dir_img+'R5E.png'), getImage(dir_img+'R6E.png'), getImage(dir_img+'R7E.png'), getImage(dir_img+'R8E.png'), getImage(dir_img+'R9E.png'), getImage(dir_img+'R10E.png'), getImage(dir_img+'R11E.png')]
    walkLeft =  [getImage(dir_img+'L1E.png'), getImage(dir_img+'L2E.png'), getImage(dir_img+'L3E.png'), getImage(dir_img+'L4E.png'), getImage(dir_img+'L5E.png'), getImage(dir_img+'L6E.png'), getImage(dir_img+'L7E.png'), getImage(dir_img+'L8E.png'), getImage(dir_img+'L9E.png'), getImage(dir_img+'L10E.png'), getImage(dir_img+'L11E.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 20
        self.visible = True

    def draw(self,win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount //3], (self.x, self.y))
                self.walkCount += 1

            pygame.draw.rect(win, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0,128,0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            #pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self,damage = 1):
        if self.health > 0:
            self.health -= damage
        else:
            self.visible = False
        print('hit')

def redrawGameWindow():
    Screen.blit(bg, (0,0))
    text = font.render('Score: ' + str(score), 1, (0,0,0))
    Screen.blit(text, (350, 10))
    man.draw(Screen)
    goblin.draw(Screen)
    for bullet in bullets:
        bullet.draw(Screen)
    
    pygame.display.update()

font = pygame.font.SysFont('comicsans', 30, True)
man = player(x=200, y=510, width=24,height=24)
goblin = enemy(x=100, y=510, width=24, height=24,end=450)
shootLoop = 0
bullets = []
run = True

while run:
    clock.tick(27)

    if goblin.visible == True:
        if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1]:
            if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
                man.hit()
                score -= 5
    
    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    for bullet in bullets:
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
            if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                hitSound.play()
                goblin.hit()
                score += 1
                bullets.pop(bullets.index(bullet))
                
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootLoop == 0:
        if man.left:
            facing = -1
        else:
            facing = 1
            
        if len(bullets) < 5:
            bullets.append(projectile(round(man.x + man.width //2), round(man.y + man.height//2), 6, (0,0,0), facing))

        shootLoop = 1

    if keys[pygame.K_a] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_d] and man.x < 500 - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0
        
    if not(man.isJump):
        if keys[pygame.K_w]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10
            
    redrawGameWindow()

pygame.quit()