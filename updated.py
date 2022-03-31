#Imports
import pygame
pygame.init()

game = ["worldy", "Level", "os", "ALPHA", "enemy_list", "world"]
    
class Platform(pygame.sprite.Sprite):
    def __init__(self, xloc, yloc, imgw, imgh, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(game[2].path.join('images', img)).convert()
        self.image.convert_alpha()
        self.image.set_colorkey(game[3])
        self.rect = self.image.get_rect()
        self.rect.y = yloc
        self.rect.x = xloc

def ground(lvl,x,y,w,h):
    ground_list = pygame.sprite.Group()
    if lvl == 1:
        ground = Platform = (x,y,w,h,'drawing.svg')
        ground_list.add(ground)

    if lvl == 2:
        print("Level " + str(lvl) )

    return ground_list

def platform( lvl ):
    plat_list = pygame.sprite.Group()

    if lvl == 1:
        plat = Platform = (200,  game[0]-97-128, 285,67,'drawing.svg')
        plat_list.add(plat)
       
        return plat_list

    ground_list = game[1].ground(1, 0, game[0]-97, 1080, 97)
    plat_list = game[1].platform(1)

    game[4].draw(game[5])  # refresh enemies
    ground_list.draw(game[5])  # refresh ground
    plat_list.draw(game[5])  # refresh platforms