import random
import pygame
import Tileset

class Tilemap(object):
    def __init__(self):
        self.tileset = Tileset.Tileset("~/Schreibtisch/Bilder2019/unchainedPhoenix.png", (255, 0, 255), 32, 32)
        self.tileset.add_tile("grass", 0, 0)
        self.tileset.add_tile("mud", 32, 0)
        self.tileset.add_tile("water", 64, 0)
        self.tileset.add_tile("block", 0, 32)

        self.camera_x = 0
        self.camera_y = 0

        self.width = 30
        self.height = 25

        self.tiles = list()

        for i in range(0, self.height):
            self.tiles.append(list())

        for j in range(0, self.width):
            x = random.randint(0, 4)
            if x == 0:
                self.tiles[i].append("grass")
            elif x == 1:
                self.tiles[i].append("water")
            elif x == 2:
                self.tiles[i].append("mud")
            else:
                self.tiles[i].append("block")

    def render(self, screen):
        for y in range(0, int(screen.get_height() / self.tileset.tile_height) + 1):
            ty = y + self.camera_y
            if ty >= self.height or ty < 0:
                continue
            line = self.tiles[ty]


            for x in range(0, int(screen.get_width() / self.tileset.tile_width) + 1):
                 tx = x + self.camera_x
                 if tx >= self.width or tx < 0:
                    continue

                 tilename = line[tx]

                 tile = self.tileset.get_tile(tilename)

                 if tile is not None:
                     screen.blit(self.tileset.image, (x * self.tileset.tile_width, y * self.tileset.tile_height))

    def handle_input(self, key):
        if key == pygame.K_LEFT:
            self.camera_x += 1
        if key == pygame.K_RIGHT:
            self.camera_x -= 1
        if key == pygame.K_UP:
            self.camera_y += 1
        if key == pygame.K_DOWN:
            self.camera_y -= 1
