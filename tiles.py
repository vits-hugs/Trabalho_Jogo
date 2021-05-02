import pygame, csv, os

import inimigo
#Código do Mapa, só aceita kkk

class Tile(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('Assets',image))
        self.image = pygame.transform.scale(self.image,(32,32))
        # Manual load in: self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
    

       

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))


class Ground(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('Assets',image))
        self.image = pygame.transform.scale(self.image,(32,32))
        self.x,self.y = x,y
        # Manual load in: self.image = pygame.image.load(image)
      

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

class TileMap():
    def __init__(self, filename):
        self.inimigos = []
        self.tile_size = 32
        self.start_x, self.start_y = 0, 0
        self.limit = pygame.math.Vector2(0,0)

       
       # self.spritesheet = spritesheet
        self.tiles = self.load_tiles(filename)
        self.map_surface = pygame.Surface((self.map_w, self.map_h))
        self.map_surface.set_colorkey((0, 0, 0))
        
        self.load_map()

        self.ground = []

      

    def draw_map(self, surface):
        surface.blit(self.map_surface, (0, 0))

    def load_map(self):
        for tile in self.tiles:
            tile.draw(self.map_surface)
        for ground in self.ground:
            ground.draw(self.map_surface)
        
    def read_csv(self, filename):
        map = []
        with open(os.path.join(filename)) as data:
            data = csv.reader(data, delimiter=',')
            for row in data:
                map.append(list(row))
        return map

    def load_tiles(self, filename):
        tiles = []
        self.ground = []
        slimes = []
        inimigos = []
        map = self.read_csv(filename)
        x, y = 0, 0
        for row in map:
            x = 0
            for tile in row:
                if tile == '-1':
                    self.ground.append(Ground('floor_1.png', x * self.tile_size, y * self.tile_size))
                if tile == '235':
                    self.start_x, self.start_y = x * self.tile_size, y * self.tile_size
                    self.ground.append(Ground('floor_1.png', x * self.tile_size, y * self.tile_size))
                elif tile == '491':
                    slimes.append(pygame.math.Vector2(x * self.tile_size, y * self.tile_size))
                    self.ground.append(Ground('floor_1.png', x * self.tile_size, y * self.tile_size))
                elif tile == '1':
                    inimigos.append(pygame.math.Vector2(x * self.tile_size, y * self.tile_size))
                    self.ground.append(Ground('floor_1.png', x * self.tile_size, y * self.tile_size))
                    
                elif tile == '33':
                    tiles.append(Tile('wall_mid.png', x * self.tile_size, y * self.tile_size))
                elif tile == '67':
                    tiles.append(Tile('wall_banner_green.png', x * self.tile_size, y * self.tile_size))
                else:
                    self.ground.append(Ground('floor_1.png', x * self.tile_size, y * self.tile_size))
                    # Move to next tile in current row
                x += 1

            # Move to next row
            y += 1
            # Store the size of the tile map
        #self.limit = (x*32-14*32,y*32)
        self.map_w, self.map_h = x * self.tile_size, y * self.tile_size
        self.inimigos.append(slimes)
        self.inimigos.append(inimigos)
        return tiles





