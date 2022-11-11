import pygame.sprite
from Protagonist import Protagonist
from SpriteSheet import SpriteSheet
from pytmx import load_pygame
import pytmx
WIDTH = 1600
HEIGHT = 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # Window Size
pygame.display.set_caption("Valley Map")
tiled_map = pytmx.TiledMap("/Users/kiang/PycharmProjects/pythonProject/PygameStuff/levels/TiledMapScenario1.tmx")
WIDTH = 1600
HEIGHT = 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Window Size
screen.fill((255,255,255))

# for layer in tiled_map.visible_layers:
#    print(layer)

# for x, y, image in tiled_map.get_layer_by_name('Buildings Architecture').tiles():
#     print(x) # your tile x position 32nd tile from left
#     print(y)
#     image


# note x and y give you the position of the tiles, not the actual position on the screen. For that, multiplly by the size of each tile.
# Add 2 more private variables to wk_tiles, + super, which gives u all attributes of the parent class.
tiled_map = pytmx.TiledMap("/Users/kiang/PycharmProjects/pythonProject/PygameStuff/levels/TiledMapScenario1.tmx")

# for layer in tiled_map.layers:
#     print(layer)

# print(dir(tiled_map.get_layer_by_name('Buildings Architecture'))
# print(tiled_map.get_layer_by_name('Buildings Architecture').properties)

# class NPC(pygame.sprite.Sprite):
#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self, coordinate_x, coordinate_y, image_path_param)
#         self.coordx = coordinate_x
#         self.coordy = coordinate_y
#         self.image = image_path_param

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
                
main()