import pygame

class store_sprite_instances:

    def __init__(self, surface, cols, rows, width, height):
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
        for i in range(self.rows):  # Height
            for j in range(self.cols):  # Width
                if i == 0:
                    self.image_store_down.append(self.surface.subsurface((j * self.width, i * self.height), (self.width, self.height)))
                elif i == 1:
                    self.image_store_left.append(self.surface.subsurface((j * self.width, i * self.height), (self.width, self.height)))
                elif i == 2:
                    self.image_store_right.append(self.surface.subsurface((j * self.width, i * self.height), (self.width, self.height)))
                else:
                    self.image_store_up.append(self.surface.subsurface((j * self.width, i * self.height), (self.width, self.height)))
        self.direction_sprites['move_left'] = self.image_store_left
        self.direction_sprites['move_right'] = self.image_store_right
        self.direction_sprites['move_up'] = self.image_store_up
        self.direction_sprites['move_down'] = self.image_store_down
        return self.direction_sprites
