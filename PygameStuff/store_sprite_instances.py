import pygame

class store_sprite_instances:

    def __init__(self, surface, cols, rows, width, height, ):
        self.surface = surface
        self.direction_sprites = {}
        self.image_store_up = []
        self.image_store_down = []
        self.image_store_left = []
        self.image_store_right = []
        self.cols = cols
        self.rows = rows
        self.width = width
        self.height = height

    def sprite_dict(self):
        if self.cols == 3 and self.rows == 4:
            for i in range(self.rows):  # Height
                for j in range(self.cols):  # Width
                    if i == 0:
                        self.image_store_down.append(self.surface.subsurface((j * self.width, i * self.height), (self.width, self.height)).convert_alpha())
                    elif i == 1:
                        self.image_store_left.append(self.surface.subsurface((j * self.width, i * self.height), (self.width, self.height)).convert_alpha())
                    elif i == 2:
                        self.image_store_right.append(self.surface.subsurface((j * self.width, i * self.height), (self.width, self.height)).convert_alpha())
                    else:
                        self.image_store_up.append(self.surface.subsurface((j * self.width, i * self.height), (self.width, self.height)).convert_alpha())
            self.direction_sprites['move_left'] = self.image_store_left
            self.direction_sprites['move_right'] = self.image_store_right
            self.direction_sprites['move_up'] = self.image_store_up
            self.direction_sprites['move_down'] = self.image_store_down
            return self.direction_sprites
        # elif self.cols == 4 and self.rows == 4 and self.width != 52: # attack stance frame width
        #     for i in range(self.rows):  # Height
        #         for j in range(self.cols):  # Width
        #             if i == 0:
        #                 self.image_store_down.append(self.surface.subsurface((j * self.width, i * self.height), (self.width, self.height)).convert_alpha())
        #             elif i == 1:
        #                 self.image_store_left.append(self.surface.subsurface((j * self.width, i * self.height), (self.width, self.height)).convert_alpha())
        #             elif i == 2:
        #                 self.image_store_right.append(self.surface.subsurface((j * self.width, i * self.height), (self.width, self.height)).convert_alpha())
        #             else:
        #                 self.image_store_up.append(self.surface.subsurface((j * self.width, i * self.height), (self.width, self.height)).convert_alpha())
        #     self.direction_sprites['attack_left'] = self.image_store_left
        #     self.direction_sprites['attack_right'] = self.image_store_right
        #     self.direction_sprites['alert_left'] = self.image_store_up
        #     self.direction_sprites['alert_right'] = self.image_store_down
        #     return self.direction_sprites
            
        elif self.cols == 4 and self.rows == 4 and self.width == 52: # boxing frame width
            for i in range(self.rows):  # Height
                for j in range(self.cols):  # Width
                    if i <= 1:
                        self.image_store_left.append(self.surface.subsurface((j * self.width, i * self.height), (self.width, self.height)).convert_alpha())
                    elif i > 1:
                        self.image_store_right.append(self.surface.subsurface((j * self.width, i * self.height), (self.width, self.height)).convert_alpha())
            self.direction_sprites['attack_left'] = self.image_store_left
            self.direction_sprites['attack_right'] = self.image_store_right
            return self.direction_sprites
