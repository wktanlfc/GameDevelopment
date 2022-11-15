import pygame
import os
import random
import time
from SpriteSheet import SpriteSheet
from Protagonist import Protagonist
from Camera import CameraGroup
import pytmx
from ObjectSprites import ObjectSprites , CollisionSprites
WIDTH = 1600
HEIGHT = 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # Window Size
pygame.display.set_caption("Valley Map")

tiled_map = pytmx.TiledMap("/Users/kiang/PycharmProjects/pythonProject/PygameStuff/levels/TiledMapScenario1.tmx")

# Houses
# Width = 6-1, Height = 4 Start positions
house1 = ObjectSprites(6,5,20,53)
house2 = ObjectSprites(6,5,34,53)
house3 = ObjectSprites(6,5,54,53)
house4 = ObjectSprites(6,5,70,53)
house5 = ObjectSprites(6,5,66,39)
house6 = ObjectSprites(6,5,18,39)
house7 = ObjectSprites(6,5,32,39)
house8 = ObjectSprites(6,5,50,39)
house9 = ObjectSprites(6,5,24,27)
house10 = ObjectSprites(6,5,40,27)
house11 = ObjectSprites(6,5,70,27)
#Load Images
main_map = pygame.image.load(
    "/Users/kiang/PycharmProjects/pythonProject/PygameStuff/levels/TiledMapScenario1.png").convert()  # surface

# Load sprites ----------------------------------------------------------------------
ObjectsGroup = pygame.sprite.Group()
CollisionGroup = pygame.sprite.Group()
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

# For PYTMX Collision placement... --------------------------------------
for x, y, image in tiled_map.get_layer_by_name('Collisions').tiles():
    _c = CollisionSprites(1,1,x,y)
    CollisionGroup.add(_c)
    # break
# ------------------------------------------------------------------------
def redraw():
    MyCamera.custom_draw(player)
    # Blitting houses onto screen
    MyCamera.display_surface.blit(house1.image, (house1.rect.x - MyCamera.offset.x , house1.rect.y - MyCamera.offset.y))
    MyCamera.display_surface.blit(house2.image, (house2.rect.x - MyCamera.offset.x , house2.rect.y - MyCamera.offset.y))
    MyCamera.display_surface.blit(house3.image, (house3.rect.x - MyCamera.offset.x , house3.rect.y - MyCamera.offset.y))
    MyCamera.display_surface.blit(house4.image, (house4.rect.x - MyCamera.offset.x , house4.rect.y - MyCamera.offset.y))
    MyCamera.display_surface.blit(house5.image, (house5.rect.x - MyCamera.offset.x , house5.rect.y - MyCamera.offset.y))
    MyCamera.display_surface.blit(house6.image, (house6.rect.x - MyCamera.offset.x , house6.rect.y - MyCamera.offset.y))
    MyCamera.display_surface.blit(house7.image, (house7.rect.x - MyCamera.offset.x , house7.rect.y - MyCamera.offset.y))
    MyCamera.display_surface.blit(house8.image, (house8.rect.x - MyCamera.offset.x , house8.rect.y - MyCamera.offset.y))
    MyCamera.display_surface.blit(house9.image, (house9.rect.x - MyCamera.offset.x , house9.rect.y - MyCamera.offset.y))
    MyCamera.display_surface.blit(house10.image,(house10.rect.x - MyCamera.offset.x , house10.rect.y - MyCamera.offset.y))
    MyCamera.display_surface.blit(house11.image,(house11.rect.x - MyCamera.offset.x , house11.rect.y - MyCamera.offset.y))
    for obj in CollisionGroup:
        MyCamera.display_surface.blit(obj.image, (obj.rect.x - MyCamera.offset.x , obj.rect.y - MyCamera.offset.y))
    MyCamera.update()
    pygame.display.update()                            # Update screen position

def main():
    run = True
    FPS = 60
    clock = pygame.time.Clock()
    while run:
        # print(player.rect) # 32 by 64 bit
        # print(_c.rect) # 160 x 160
        # print(_c.image)
        clock.tick(FPS)                                 # Gets you the time in milliseconds since pygame.init() was called
# Check events, can look up events in the pygame website
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
# This is set to reset the animations of other directional booleans from the last key press.
# To prevent bug of animations using the previous keypress direction.
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
    
            for objects in CollisionGroup:
                if player.rect.colliderect(objects):
                    player.rect.x -= player.velocity_x
                    player.rect.y -= player.velocity_y

            redraw()
            pygame.display.flip()
            
main()

# print('Display screen size is :' + str(MyCamera.display_surface))
# print('Protagonist is at' + str(player.rect)) # Adding it here lets you see the coordinates of where your character is.
# print(MyCamera.main_map_rect.center)


