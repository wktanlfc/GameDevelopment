import pygame
import os
import random
import time
from SpriteSheet import SpriteSheet
from Protagonist import Protagonist
from store_sprite_instances import store_sprite_instances

WIDTH = 1280
HEIGHT = 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Valley Map")
# Load Images
main_map = pygame.image.load("/Users/kiang/PycharmProjects/pythonProject/PygameStuff/levels/TiledMapScenario1.png").convert()  # surface
# sample = pygame.transform.scale(sample, (WIDTH, HEIGHT))

# Movement Bools
move_left = False
move_right = False
move_up = False
move_down = False

# Load sprites
all_sprites = pygame.sprite.Group()
player = Protagonist()
all_sprites.add(player)


def redraw():
    WIN.fill((255, 255, 255))
    WIN.blit(main_map, (-500, -750))
    all_sprites.draw(WIN)
    all_sprites.update()  # Update sprite position
    pygame.display.update() # Update screen position


def main():
    run = True
    FPS = 60
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        # Check events, can look up events in the pygame website
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            redraw()


main()
