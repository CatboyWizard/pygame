import pygame
from typing import Tuple
import sys
import os

'''
Variables
'''

worldx = 960
worldy = 720
fps = 40  # frame rate
ani = 4  # animation cycles
world = pygame.display.set_mode([worldx, worldy])

BLUE = (25, 25, 200)
BLACK = (23, 23, 23)
WHITE = (254, 254, 254)
ALPHA = (0, 255, 0)

'''
Objects
'''


class Player(pygame.sprite.Sprite):
    """
    Spawn a player
    """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for i in range(1, 5):
            img = pygame.image.load('C:\\Users\\mchugh_kevin\\Desktop\\python4\\pygame\\images\\hero1.png')
            img.convert_alpha()  # optimise alpha
            img.set_colorkey(ALPHA)  # set alpha
            self.images.append(img)
            self.image = self.images[0]
            self.rect = self.image.get_rect()


'''
Setup
'''

backdrop = pygame.image.load('C:\\Users\\mchugh_kevin\\Desktop\\python4\\pygame\\images\\drawing3.jpg')
clock = pygame.time.Clock()
pygame.init()
backdropbox = world.get_rect()
main = True

player = Player()  # spawn player
player.rect.x = 0  # go to x
player.rect.y = 0  # go to y
player_list = pygame.sprite.Group()
player_list.add(player)


'''
Main Loop
'''

while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            try:
                sys.exit()
            finally:
                main = False

        if event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                pygame.quit()
            try:
                sys.exit()
            finally:
                main = False
    world.blit(backdrop, backdropbox)
    player_list.draw(world)
    pygame.display.flip()
    clock.tick(fps)


'''
NPC Dialouge
'''


NPC = ["NPC_HIT_RECT", "vec", "Player", "Obstacle", "Enemies", "Camera"]


class NPC(pygame.sprite.Sprite):

    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.npc_img
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.hit_rect = NPC[0]
        self.hit_rect.center = self.rect.center
        self.vel = NPC[1](0,0)
        self.pos = NPC[1](x, y)
        self.rect.center = self.pos

    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.npc = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        for tile_object in self.map.tmxdata.objects:
            if tile_object.name == 'Player Spawn':
                self.player = NPC[2](self, tile_object.x, tile_object.y)
            if tile_object.name == 'NPC':
                NPC(self, tile_object.x, tile_object.y)
                NPC[3](self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)

            if tile_object.name == 'Enemy':
                NPC[4](self, tile_object.x, tile_object.y)
            if tile_object.name == 'Wall':
                NPC[3](self, tile_object.x, tile_object.y, tile_object.width, tile_object.height)
        self.camera = NPC[5](self.map.width, self.map.height)
        self.draw_debug = False
        self.run()

