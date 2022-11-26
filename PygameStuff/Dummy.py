import random
from SpriteSheet import SpriteSheet
from pytmx import load_pygame
from store_sprite_instances import store_sprite_instances
import pygame
from NPC import NPC_guard


# Load Images
knight = pygame.image.load("/Users/kiang/PycharmProjects/pythonProject/PygameStuff/Player/HighResRomanKnight.png").convert()  #surface 52 by 72
random_guard_img_instances = store_sprite_instances(knight, 3, 4, 52, 72, NPC = True)
random_guard_imgs = random_guard_img_instances.sprite_dict()

class Dummy(pygame.sprite.Sprite):
    def __init__(self, width, height, image_param = None): # original sprite parameters
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(width,height, 32, 32)  # Since get.image.rect returns 52 x 72, dont use. create own 32 x 64 rect.
        self.rect.centerx = int(width * 32)
        self.rect.centery = int(height * 32)
        if image_param is None:
            self.image = pygame.image.load("/Users/kiang/PycharmProjects/pythonProject/PygameStuff/levels/TX Plant.png").convert_alpha()
        else:
            self.image = image_param

class NPC(Dummy):
    def __init__(self, width, height, image_param = None):
        super(NPC, self).__init__(width, height, image_param = None)
        self.move_time = None
        self.image = random_guard_imgs.get('move_down')[0]
        self.facing_left, self.facing_right, self.facing_up, self.facing_down = False, False, False, False
        self.update_timestamp = 0
        self.current_frame = 0
        self.movement_direction = {"1": "Up", "2": "Down", "3": "Left", "4": "Right", "5": "Idle"}
        self.velocity_x = 0
        self.velocity_y = 0
        self.speed = 4
        self.prev_dir_counter = 50
        self.previous_choice = None
    
    def move(self):
        # print("Current Update:" + str(pygame.time.get_ticks()))
        # print("Previous Update:" + str(self.update_timestamp))
        self.move_time = random.randrange(1000, 2000, 1)
        self.choice = self.movement_direction.get(str(random.randint(1, 5)))
        self.current_frame = (self.current_frame + 1) % len(random_guard_imgs.get('move_up'))
        if self.prev_dir_counter > 0 and self.previous_choice is not None:
            self.choice = self.previous_choice
            self.prev_dir_counter -= 1
        else:
            self.prev_dir_counter = 50
        if self.choice == "Left":
            self.velocity_x = -self.speed
        if self.choice == "Right":
            self.velocity_x = self.speed
        if self.choice == "Up":
            self.velocity_y = -self.speed
        if self.choice == "Down":
            self.velocity_y = +self.speed

        if self.update_timestamp <= pygame.time.get_ticks():
            self.rect.centerx += self.velocity_x
            self.rect.centery += self.velocity_y
        self.update_timestamp = pygame.time.get_ticks() - self.move_time
        self.previous_choice = self.choice

    def animate(self):
        if self.choice == "Left":
            self.image = random_guard_imgs.get('move_left')[self.current_frame]
        if self.choice == "Right":
            self.image = random_guard_imgs.get('move_right')[self.current_frame]
        if self.choice == "Up":
            self.image = random_guard_imgs.get('move_up')[self.current_frame]
        if self.choice == "Down":
            self.image = random_guard_imgs.get('move_down')[self.current_frame]
    
    def update(self):
        self.move()
        self.animate()
















if __name__ == "__main__":
    print("Hello World")
    WIN = pygame.display.set_mode((1600, 1000))
    TestingGroup = pygame.sprite.Group()
    TestDummy = Dummy(32,32)
    NPC = NPC(1600/2/32,1000/2/32)
    TestingGroup.add(NPC)
    pygame.display.update()
    pygame.init()


    def main():
        
        run = True
        FPS = 60
        clock = pygame.time.Clock()
        pygame.time.set_timer(pygame.USEREVENT, 100)
        elapsed_time = 0
        tick_time = pygame.time.get_ticks()/1000
        time_interval = random.randint(3,5)
        while run:
            clock.tick(FPS)  # Gets you the time in milliseconds since pygame.init() was called
            elapsed_time += tick_time
            pygame.display.flip()
            # WIN.fill((0, 0, 0))
            # TestingGroup.update()
            # WIN.blit(NPC.image, NPC.rect)
            """
            if elapsed time from init passes random time_interval,
            call update to NPCs making them move. Reset the elapsed time again.
            """
            # print(clock.get_time())
            # Number of miliseconds between 2 clock.ticks0
            # print(clock.get_time()) # find a way to get delta time, then update every randomint*deltatime
            # t = pygame.time.get_ticks()
            # print("t is :" + str(t))
            # getticksoflastframe = 0
            # delta_time_holder = (t - getticksoflastframe) / 1000
            # getticksoflastframe = t /1000
            # print(getticksoflastframe)
            # print(NPC.updt_timestamp)
    
    
    
    
            # Check events, can look up events in the pygame website
            for event in pygame.event.get():
                if event.type == pygame.USEREVENT:
                    WIN.fill((0, 0, 0))
                    TestingGroup.update()
                    WIN.blit(NPC.image, NPC.rect)
                if event.type == pygame.QUIT:
                    run = False
    
    
                    
    main()