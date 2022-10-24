import pygame
import os
import random
import time
from SpriteSheet import SpriteSheet
from Protagonist import Protagonist
from pytmx import load_pygame


class CameraGroup(pygame.sprite.Group):
    def __init__(self, main_map_surface):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.main_map = main_map_surface
        self.main_map_rect = main_map_surface.get_rect() # 0,0,3200,3200 coordingates
        
        # camera offset
        self.offset = pygame.math.Vector2()
        self.half_w = self.display_surface.get_size()[0] // 2 # 800/ 2 = 400
        self.half_h = self.display_surface.get_size()[1] // 2 # 600/ 2 = 300
    
    def center_target_camera(self, target):
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_h
        
    def custom_draw(self, target):
        self.center_target_camera(target)
        #Display the Map sprite
        self.display_surface.blit(self.main_map, (self.main_map_rect.x - self.offset.x , self.main_map_rect.y - self.offset.y ))
        #Display the character sprite
        self.display_surface.blit(target.image, (target.rect.centerx - self.offset.x,target.rect.centery - self.offset.y) )
