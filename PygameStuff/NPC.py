import pygame.sprite
from Protagonist import Protagonist
from SpriteSheet import SpriteSheet
from pytmx import load_pygame
from store_sprite_instances import store_sprite_instances
import random
WIN = pygame.display.set_mode((1600, 1000))

# # Load Images
# knight = pygame.image.load(
#     "/Users/kiang/PycharmProjects/pythonProject/PygameStuff/Player/HighResRomanKnight.png").convert()  # surface 52 by 72
# random_guard_img_instances = store_sprite_instances(knight, 3, 4, 52, 72, NPC = True)
# random_guard_imgs = random_guard_img_instances.sprite_dict()

class NPC_guard(Protagonist):
    """Subclass of Protagonist, inherits all movement attributes, health, etc
    """
    # @override
    def __init__(self, tile_pos_x, tile_pos_y):
        super().__init__(tile_pos_x, tile_pos_y)
        self.image = random_guard_imgs.get('move_down')[0] # Correct, nothing wrong with this
        self.speed = 4
        self.movement_direction = {"1":"Up"
            ,"2":"Down"
            ,"3":"Left"
            ,"4":"Right"
            ,"5":"Idle"}
        self.updt_timestamp = 0
    
    def update(self):
        self.velocity_x = 0
        self.velocity_y = 0
        self.random_duration = random.randrange(3000, 5000, 1)
        self.choice = self.movement_direction.get(str(random.randint(1, 5)))
        print("Current Update:" + str(pygame.time.get_ticks()))
        print("Previous Update:" + str(self.updt_timestamp))
        # self.set_state()
        self.move()
        # self.animate()
        self.updt_timestamp = pygame.time.get_ticks()
        
    def move(self):
        
        if self.choice == "Left":
            self.velocity_x = -self.speed
            self.facing_left = True
        if self.choice == "Right":
            self.velocity_x = self.speed
            self.facing_right = True
        if self.choice == "Up":
            self.velocity_y = -self.speed
            self.facing_up = True
        if self.choice == "Down":
            self.velocity_y = self.speed
            self.facing_down = True
        while self.updt_timestamp + self.random_duration > pygame.time.get_ticks():
            self.rect.centerx += self.velocity_x
            self.rect.centery += self.velocity_y
            self.current_frame = (self.current_frame + 1) % len(random_guard_imgs.get('move_up'))
            if self.move_left:
                self.image = random_guard_imgs.get('move_left')[self.current_frame]
            if self.move_right:
                self.image = random_guard_imgs.get('move_right')[self.current_frame]
            if self.move_up:
                self.image = random_guard_imgs.get('move_up')[self.current_frame]
            if self.move_down:
                self.image = random_guard_imgs.get('move_down')[self.current_frame]


            
    # def set_state():
    #     super(NPC_guard, self).set_state()
    #
    # def animate(self):
    #     now = pygame.time.get_ticks()
        # if self.default_state == 'Idle':
        #     if self.facing_down:
        #         self.image = random_guard_imgs.get('move_down')[0]
        #     if self.facing_up:
        #         self.image = random_guard_imgs.get('move_up')[0]
        #     if self.facing_left:
        #         self.image = random_guard_imgs.get('move_left')[0]
        #     if self.facing_right:
        #         self.image = random_guard_imgs.get('move_right')[0]
        
        # if self.default_state == 'Moving':
        #     if now - self.updt_timestamp:
        #         self.last_updated = now
        #         self.current_frame = (self.current_frame + 1) % len(random_guard_imgs.get('move_up'))
        #         if self.move_left:
        #             self.image = random_guard_imgs.get('move_left')[self.current_frame]
        #         if self.move_right:
        #             self.image = random_guard_imgs.get('move_right')[self.current_frame]
        #         if self.move_up:
        #             self.image = random_guard_imgs.get('move_up')[self.current_frame]
        #         if self.move_down:
        #             self.image = random_guard_imgs.get('move_down')[self.current_frame]
        





