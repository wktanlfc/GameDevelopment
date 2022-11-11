import pygame
import os
import random
import time
from SpriteSheet import SpriteSheet
from Protagonist import Protagonist
from pytmx import load_pygame
from Camera import CameraGroup
import pytmx
from ObjectSprites import ObjectSprites
WIDTH = 1600
HEIGHT = 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # Window Size
pygame.display.set_caption("Valley Map")

# Houses
# Width = 6-1, Height = 5 Start positions
house1 = ObjectSprites(5,5,20,51)
house2 = ObjectSprites(5,5,34,51)
house3 = ObjectSprites(5,5,54,51)
house4 = ObjectSprites(5,5,70,51)
house5 = ObjectSprites(5,5,66,37)
house6 = ObjectSprites(5,5,18,37)
house7 = ObjectSprites(5,5,32,37)
house8 = ObjectSprites(5,5,50,37)
house9 = ObjectSprites(5,5,24,25)
house10 = ObjectSprites(5,5,40,25)
house11 = ObjectSprites(5,5,70,25)
#Load Images
main_map = pygame.image.load(
    "/Users/kiang/PycharmProjects/pythonProject/PygameStuff/levels/TiledMapScenario1.png").convert()  # surface
# house_sample = pygame.Surface((6*32,5*32), (54*32,53*32));
# Load sprites
ObjectsGroup = pygame.sprite.Group()
MyCamera = CameraGroup(main_map) # sprite.Group subclass + surface_param for main map.
player = Protagonist(57,80)
MyCamera.add(player)
ObjectsGroup.add(house1)
ObjectsGroup.add(house2)
ObjectsGroup.add(house3)
ObjectsGroup.add(house4)
ObjectsGroup.add(house5)
ObjectsGroup.add(house6)
ObjectsGroup.add(house7)
ObjectsGroup.add(house8)
ObjectsGroup.add(house9)
ObjectsGroup.add(house10)
ObjectsGroup.add(house11)

def redraw():
    MyCamera.custom_draw(player)
    #Bliting houses onto screen
    # MyCamera.display_surface.blit(house1.image, (20*32 - MyCamera.offset.x,53*32 - MyCamera.offset.y))
    # MyCamera.display_surface.blit(house2.image, (34*32 - MyCamera.offset.x,53*32 - MyCamera.offset.y))
    # MyCamera.display_surface.blit(house3.image, (54*32 - MyCamera.offset.x,53*32-  MyCamera.offset.y))
    # MyCamera.display_surface.blit(house4.image, (70*32 - MyCamera.offset.x,53*32 - MyCamera.offset.y))
    # MyCamera.display_surface.blit(house5.image, (18*32 - MyCamera.offset.x,39*32 - MyCamera.offset.y))
    # MyCamera.display_surface.blit(house6.image, (32*32 - MyCamera.offset.x,39*32 - MyCamera.offset.y))
    # MyCamera.display_surface.blit(house7.image, (50*32 - MyCamera.offset.x,39*32-  MyCamera.offset.y))
    # MyCamera.display_surface.blit(house8.image, (66*32 - MyCamera.offset.x,39*32 - MyCamera.offset.y))
    # MyCamera.display_surface.blit(house9.image, (24*32 - MyCamera.offset.x,27*32-  MyCamera.offset.y))
    # MyCamera.display_surface.blit(house1.image, (70*32 - MyCamera.offset.x,26*32 - MyCamera.offset.y))
    MyCamera.update()
    pygame.display.update()  # Update screen position
    # ObjectsGroup.update()
def main():
    run = True
    FPS = 60
    clock = pygame.time.Clock()
    while run:
        
        clock.tick(FPS)  # Gets you the time in milliseconds since pygame.init() was called
        
        # Check events, can look up events in the pygame website
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # This is set to reset the animations of other directional booleans from the last key press. To prevent bug of animations using the previous keypress direction.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.move_left, player.move_up, player.move_down , player.move_right = True, False, False, False
                    player.facing_left, player.facing_up, player.facing_down, player.facing_right = True, False, False, False
                if event.key == pygame.K_d:
                    player.move_left, player.move_up, player.move_down , player.move_right = False, False, False, True
                    player.facing_left, player.facing_up, player.facing_down, player.facing_right = False, False, False, True
                if event.key == pygame.K_w:
                    player.move_left, player.move_up, player.move_down , player.move_right = False, True, False, False
                    player.facing_left, player.facing_up, player.facing_down, player.facing_right = False, True, False, False
                if event.key == pygame.K_s:
                    player.move_left, player.move_up, player.move_down , player.move_right = False, False, True, False
                    player.facing_left, player.facing_up, player.facing_down, player.facing_right = False, False, True, False
                if event.key == pygame.K_SPACE:
                    player.move_left, player.move_up, player.move_down , player.move_right, player.attacking = False, False, False, False, True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        player.move_left , player.facing_left = False, True
                    if event.key == pygame.K_d:
                        player.move_right , player.facing_right = False, True
                    if event.key == pygame.K_w:
                        player.move_up , player.facing_up = False, True
                    if event.key == pygame.K_s:
                        player.move_down , player.facing_down = False, True
                    if event.key == pygame.K_SPACE:
                        player.attacking = False
            
            for house in ObjectsGroup:
                if player.rect.colliderect(house):
                    player.rect.x -= player.velocity_x
                    player.rect.y -= player.velocity_y
            redraw()
            pygame.display.flip()
            
main()

# print(type(player))
# print('Display screen size is :' + str(MyCamera.display_surface))
# print('Protagonist is at' + str(player.rect)) # Adding it here lets you see the coordinates of where your character is.
# print(MyCamera.main_map_rect.center)
# if player.rect.colliderect(house0.rect):
#     print('Dieliao')
# else:
#     print('Noleh')


