import pygame, csv, os

import inimigo
#Código do Mapa, só aceita kkk

class Tile(pygame.sprite.Sprite): # Cria uma classe de quadradinhos tile
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('Assets',image))
        self.image = pygame.transform.scale(self.image,(32,32))
        

        #com retangulo tirado da imagem q é usado pra colisão
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

       
    #função que desenha as tile
    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))


class Ground(pygame.sprite.Sprite): #criei classe só pra fazer o chão
    def __init__(self, image, x, y):#a diferença é que ela n tem colisor
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('Assets',image))
        self.image = pygame.transform.scale(self.image,(32,32))
        self.x,self.y = x,y
        


      

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

#Classe que cuida do mapa
class TileMap():
    def __init__(self, filename):
        self.inimigos = []
        self.tile_size = 32
        self.start_x, self.start_y = 0, 0

       
       # self.spritesheet = spritesheet
        self.tiles = self.load_tiles(filename) #vai ler o arquivo de mapa 
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
        
    def read_csv(self, filename): #le o arquivo csv 
        map = []
        with open(os.path.join(filename)) as data:#le o numero e até a virgula
            data = csv.reader(data, delimiter=',')
            for row in data:
                map.append(list(row))   #da uma matriz com cada linha
        return map

    def load_tiles(self, filename):#Cria Array com todos as tiles
        tiles = []                  #Além dos Arrays com a posição dos inimigo
        self.ground = []
        slimes = []
        inimigos = []
        map = self.read_csv(filename)
        x, y = 0, 0
        for row in map:#pra cada linha
            x = 0
            for tile in row:#verfica o numero e cola na posição x
                if tile == '-1':
                    self.ground.append(Ground('rian.jpg', x * self.tile_size, y * self.tile_size))
                if tile == '235':
                    self.start_x, self.start_y = x * self.tile_size, y * self.tile_size
                    self.ground.append(Ground('rian.jpg', x * self.tile_size, y * self.tile_size))
                elif tile == '491':
                    slimes.append(pygame.math.Vector2(x * self.tile_size, y * self.tile_size))
                    self.ground.append(Ground('rian.jpg', x * self.tile_size, y * self.tile_size))
                elif tile == '1':
                    inimigos.append(pygame.math.Vector2(x * self.tile_size, y * self.tile_size))
                    self.ground.append(Ground('rian.jpg', x * self.tile_size, y * self.tile_size))
                    
                elif tile == '33':
                    tiles.append(Tile('wall_mid.png', x * self.tile_size, y * self.tile_size))
                elif tile == '67':
                    tiles.append(Tile('wall_banner_green.png', x * self.tile_size, y * self.tile_size))
                    # Move to next tile in current row
                x += 1

            # Move to next row
            y += 1# e depois vai pra proxima linha
            # Store the size of the tile map
        self.map_w, self.map_h = x * self.tile_size, y * self.tile_size #no final define tamanho do map
        self.inimigos.append(slimes)
        self.inimigos.append(inimigos)
        return tiles





