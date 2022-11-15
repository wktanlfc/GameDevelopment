import pygame.sprite

# Surface((width, height), flags=0, depth=0, masks=None) -> Surface
# Surface((width, height), flags=0, Surface) -> Surface

class ObjectSprites(pygame.sprite.Sprite):
    def __init__(self, width_in_tiles, height_in_tiles, _Xcoord, _Ycoord):
        pygame.sprite.Sprite.__init__(self)
        self.tileSize = 32
        self.w = width_in_tiles
        self.h = height_in_tiles
        self.image = pygame.Surface((self.w * self.tileSize, self.h * self.tileSize)).convert_alpha()
        # self.image.fill((0, 255, 255))
        self.rect = self.image.get_rect(topleft= (_Xcoord * self.tileSize, _Ycoord * self.tileSize))
        

class CollisionSprites(pygame.sprite.Sprite):
    def __init__(self, width_in_tiles, height_in_tiles, _Xcoord, _Ycoord):
        pygame.sprite.Sprite.__init__(self)
        self.tileSize = 32
        self.w = width_in_tiles
        self.h = height_in_tiles
        self.image = pygame.Surface((self.w * self.tileSize, self.h * self.tileSize)).convert_alpha()
        # self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect(topleft=(_Xcoord * self.tileSize, _Ycoord * self.tileSize - 32)) # -32 off the y_coordinate of each obstavle