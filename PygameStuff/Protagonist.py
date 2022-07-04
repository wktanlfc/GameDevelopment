import pygame
from pygame.draw import rect
from SpriteSheet import SpriteSheet
from store_sprite_instances import store_sprite_instances

WIDTH = 1280
HEIGHT = 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Load Images
knight = pygame.image.load("/Users/kiang/PycharmProjects/pythonProject/PygameStuff/Player/HighResRomanKnight.png").convert()  # surface 52 by 72
knight_img = store_sprite_instances(knight, 3, 4, 52, 72)
blah = knight_img.sprite_dict()

class Protagonist(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image =  self.image = blah.get('move_down')[0] # pygame.Surface((52, 72))
        self.rect = self.image.get_rect()
        self.rect.centerx = 1000 / 2
        self.rect.centery = 1000 / 2
        self.rect.bottom = 500 - 10
        self.move_left = False
        self.move_right = False
        self.move_up = False
        self.move_down = False
        
    def update(self):
        self.speedx = 0
        self.speedy = 0
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.speedx -= 4
            move_left = True
            self.image = blah.get('move_left')[0]
        if keystate[pygame.K_d]:
            self.speedx += 4
            move_right = True
            self.image = blah.get('move_right')[0]
        if keystate[pygame.K_w]:
            self.speedy -= 4
            move_up = True
            self.image = blah.get('move_up')[0]
        if keystate[pygame.K_s]:
            self.speedy += 4
            move_down = True
            self.image = blah.get('move_down')[0]
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > 1000:
            self.rect.right = 1000
        if self.rect.left < 0:
            self.rect.left = 0
