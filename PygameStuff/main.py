import pygame
import os
import random
import time
from SpriteSheet import SpriteSheet
from Protagonist import Protagonist
from pytmx import load_pygame
# from store_sprite_instances import store_sprite_instances

WIDTH = 1280
HEIGHT = 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Valley Map")
# Load Images
# main_map2 = load_pygame("/Users/kiang/PycharmProjects/pythonProject/PygameStuff/levels/TiledMapScenario1.tmx")
main_map = pygame.image.load(
    "/Users/kiang/PycharmProjects/pythonProject/PygameStuff/levels/TiledMapScenario1.png").convert()  # surface
# sample = pygame.transform.scale(sample, (WIDTH, HEIGHT))

# Load sprites
all_sprites = pygame.sprite.Group()
player = Protagonist()
all_sprites.add(player)

def redraw():
    WIN.fill((255, 255, 255))
    WIN.blit(main_map, (-1600, -1600)) #x-axis from the left -500 -750 -1350 , -1750
    all_sprites.draw(WIN)
    # WIN.blit(player.image, player.rect)
    all_sprites.update()  # Update Protagonist sprite position
    pygame.display.update()  # Update screen position


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
                    player.move_left, player.move_up, player.move_down , player.move_right, player.attacking  = False, False, False, False, True
                
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        player.move_left = False
                    if event.key == pygame.K_d:
                        player.move_right = False
                    if event.key == pygame.K_w:
                        player.move_up = False
                    if event.key == pygame.K_s:
                        player.move_down = False
            redraw()


main()
