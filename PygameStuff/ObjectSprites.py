import pygame.sprite

class ObjectSprites(pygame.sprite.Sprite):
    def __init__(self, width_in_tiles, height_in_tiles, _Xcoord, _Ycoord):
        pygame.sprite.Sprite.__init__(self)
        self.tileSize = 32
        self.w = width_in_tiles
        self.h = height_in_tiles
        self.image = pygame.Surface((self.w * self.tileSize, self.h * self.tileSize))
        # self.image = self.image.fill(255,255,255)
        self.rect = self.image.get_rect()
        self.rect.x = _Xcoord * self.tileSize
        self.rect.y = _Ycoord * self.tileSize
        
    