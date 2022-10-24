import pygame
import os
import random
import time
from SpriteSheet import SpriteSheet
from Protagonist import Protagonist
from pytmx import load_pygame
from Camera import CameraGroup

WIDTH = 1400
HEIGHT = 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # Window Size
pygame.display.set_caption("Valley Map")
scroll = [0 , 0]

#Load Images
main_map = pygame.image.load(
    "/Users/kiang/PycharmProjects/pythonProject/PygameStuff/levels/TiledMapScenario1.png").convert()  # surface

# Load sprites
MyCamera = CameraGroup(main_map) # sprite.Group subclass + surface_param for main map.
player = Protagonist()
MyCamera.add(player)


def redraw():
    MyCamera.update()
    MyCamera.custom_draw(player)
    pygame.display.update()  # Update screen position

def main():
    run = True
    FPS = 60
    clock = pygame.time.Clock()
    while run:
        # print(type(player))
        # print('Display screen size is :' + str(MyCamera.display_surface))
        # print('Protagonist is at' + str(player.rect)) # Adding it here lets you see the coordinates of where your character is.
        # print(MyCamera.main_map_rect.center)
        clock.tick(FPS)  # Gets you the time in milliseconds since pygame.init() was called

        # Check events, can look up events in the pygame website
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            #This is set to reset the animations of other directional booleans from the last key press. To prevent bug of animations using the previous keypress direction.
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
            
            redraw()
            
main()
