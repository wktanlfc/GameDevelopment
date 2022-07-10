import pygame
import os
import random
import time
from SpriteSheet import SpriteSheet
# from Protagonist import Protagonist
from store_sprite_instances import store_sprite_instances

WIDTH = 1280
HEIGHT = 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Valley Map")
# Load Images
main_map = pygame.image.load(
    "/Users/kiang/PycharmProjects/pythonProject/PygameStuff/levels/TiledMapScenario1.png").convert()  # surface
# sample = pygame.transform.scale(sample, (WIDTH, HEIGHT))

# Load Image
knight = pygame.image.load(
    "/Users/kiang/PycharmProjects/pythonProject/PygameStuff/Player/HighResRomanKnight.png").convert()  # surface 52 by 72
knight_img = store_sprite_instances(knight, 3, 4, 52, 72)
blah = knight_img.sprite_dict()


class Protagonist(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = blah.get('move_down')[0]  # pygame.Surface((52, 72))
        self.rect = self.image.get_rect()  # Get the width and the height of the surface of image above.
        self.rect.centerx = 1000/2
        self.rect.centery = 1000/2
        self.rect.bottom = 500 - 10
        self.move_left = False
        self.move_right = False
        self.move_up = False
        self.move_down = False
        self.default_state = 'Idle'  # Default Position of the character
        self.current_frame = 0  # A holder for the current frame when the ticks are runnign
        self.last_updated = 0  # To
        self.velocity_x = 0
        self.velocity_y = 0
    
    def update(self):
        self.velocity_x = 0
        self.velocity_y = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.velocity_x = -4
        if keystate[pygame.K_d]:
            self.velocity_x = 4
        if keystate[pygame.K_w]:
            self.velocity_y = -4
        if keystate[pygame.K_s]:
            self.velocity_y = 4
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y
        self.set_state()
        self.animate()
     
    def set_state(self):  # For changing default states to trigger image change in animate.
        if self.velocity_x == 0 and self.velocity_y == 0:
            self.default_state = 'Idle'
        elif self.velocity_x < 0:
            self.default_state = 'Moving Left'
        elif self.velocity_x > 0:
            self.default_state = 'Moving Right'
        elif self.velocity_y > 0:
            self_default_state = 'Moving Down'
        elif self.velocity_y < 0:
            self.default_state = 'Moving Up'
    
    def animate(self):
        now = pygame.time.get_ticks()
        if self.default_state == 'Idle':
            self.image = blah.get('move_down')[1]  # Add in a default moving image.
        else:
            if now - self.last_updated > 150:  # Check if last 200 seconds have passed. If it has passed, then
                self.last_updated = now
                self.current_frame = (self.current_frame + 1) % len(blah.get('move_up'))
                if self.move_left:  #self.default_state == 'Moving Left':
                    self.image = blah.get('move_left')[self.current_frame]
                if self.move_right: #self.default_state == 'Moving Right':
                    self.image = blah.get('move_right')[self.current_frame]
                if self.move_up: #self.default_state == 'Moving Up':
                    self.image = blah.get('move_up')[self.current_frame]
                if self.move_down: #self.default_state == 'Moving Down':
                    self.image = blah.get('move_down')[self.current_frame]


# Load sprites
all_sprites = pygame.sprite.Group()
player = Protagonist()
all_sprites.add(player)


def redraw():
    WIN.fill((255, 255, 255))
    WIN.blit(main_map, (-500, -750))
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.move_left, player.move_up, player.move_down , player.move_right = True, False, False, False
                if event.key == pygame.K_d:
                    player.move_left, player.move_up, player.move_down , player.move_right = False, False, False, True
                if event.key == pygame.K_w:
                    player.move_left, player.move_up, player.move_down , player.move_right = False, True, False, False
                if event.key == pygame.K_s:
                    player.move_left, player.move_up, player.move_down , player.move_right = False, False, True, False
                    
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        player.move_left, player.move_up, player.move_down, player.move_right = False, False, False, False
                    if event.key == pygame.K_d:
                        player.move_left, player.move_up, player.move_down, player.move_right = False, False, False, False
                    if event.key == pygame.K_w:
                        player.move_left, player.move_up, player.move_down, player.move_right = False, False, False, False
                    if event.key == pygame.K_s:
                        player.move_left, player.move_up, player.move_down, player.move_right = False, False, False, False
            redraw()


main()
