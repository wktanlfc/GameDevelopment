import pygame
from pygame.draw import rect
from SpriteSheet import SpriteSheet

# Global Variables
from store_sprite_instances import store_sprite_instances
WIDTH = 1280
HEIGHT = 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# Load Images
knight = pygame.image.load(
    "/Users/kiang/PycharmProjects/pythonProject/PygameStuff/Player/HighResRomanKnight.png").convert()  # surface 52 by 72
knight_one_two = pygame.image.load(
    "/Users/kiang/PycharmProjects/pythonProject/PygameStuff/Player/KnightOneTwoCombo2.png").convert()

knight_img = store_sprite_instances(knight, 3, 4, 52, 72)
knight_img3 = store_sprite_instances(knight_one_two, 4, 4, 52, 72)
blah = knight_img.sprite_dict()
KnightOneTwo = knight_img3.sprite_dict()


class Protagonist(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = blah.get('move_down')[0]  # pygame.Surface((52, 72))
        self.rect = self.image.get_rect()  # Get the width and the height of the surface of image above.
        self.rect.centerx = 1000 / 2
        self.rect.centery = 1000 / 2
        self.rect.bottom = 500 - 10
        self.attacking = False
        self.move_left = False
        self.move_right = False
        self.move_up = False
        self.move_down = False
        self.facing_left = False
        self.facing_right = False
        self.facing_up = False
        self.facing_down = False
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
            self.facing_left = True
        if keystate[pygame.K_d]:
            self.velocity_x = 4
            self.facing_right = True
        if keystate[pygame.K_w]:
            self.velocity_y = -4
            self.facing_up = True
        if keystate[pygame.K_s]:
            self.velocity_y = 4
            self.facing_down = True
        if keystate[pygame.K_SPACE]:
            self.attacking = True
        
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y
        self.set_state()
        self.animate()
    
    def get_frames(self):
        pass
    
    def set_state(self):  # For changing default states to trigger image change in animate.
        if self.velocity_x == 0 and self.velocity_y == 0 and self.attacking is False:
            self.default_state = 'Idle'
        elif self.velocity_x == 0 and self.velocity_y == 0 and self.attacking:
            self.default_state = 'Alert'
        else:
            self.default_state = 'Moving'
    
    def animate(self):
        now = pygame.time.get_ticks()
        if self.default_state == 'Idle':
            if self.facing_down:
                self.image = blah.get('move_down')[1]
            if self.facing_up:
                self.image = blah.get('move_up')[1]
            if self.facing_left:
                self.image = blah.get('move_left')[1]
            if self.facing_right:
                self.image = blah.get('move_right')[1]
        
        elif self.default_state == "Alert":
            if now - self.last_updated > 60:
                self.last_updated = now
                self.current_frame = (self.current_frame + 1) % len(KnightOneTwo.get('attack_left'))
                if self.attacking and self.facing_left:
                    self.image = KnightOneTwo.get('attack_left')[self.current_frame]
                if self.attacking and self.facing_right:
                    self.image = KnightOneTwo.get('attack_right')[self.current_frame]
        
        elif self.default_state == 'Moving':
            if now - self.last_updated > 150:
                self.last_updated = now
                self.current_frame = (self.current_frame + 1) % len(blah.get('move_up'))
                if self.move_left:  # self.default_state == 'Moving Left':
                    self.image = blah.get('move_left')[self.current_frame]
                if self.move_right:  # self.default_state == 'Moving Right':
                    self.image = blah.get('move_right')[self.current_frame]
                if self.move_up:  # self.default_state == 'Moving Up':
                    self.image = blah.get('move_up')[self.current_frame]
                if self.move_down:  # self.default_state == 'Moving Down':
                    self.image = blah.get('move_down')[self.current_frame]
