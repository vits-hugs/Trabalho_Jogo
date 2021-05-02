import pygame
import os
from inimigo import Inimigo
from player import player
#Downloads\JogoTop-master\JogoTop-master

class mago(Inimigo):
    def __init__(self,pos_x,pos_y):
        super().__init__(pos_x,pos_y)
        pygame.mixer.init()
        self.delay = 301
        self.vida = 2
        self.image = pygame.image.load(os.path.join('Assets','Monstros','mago.png'))
        self.image = pygame.transform.scale(self.image,(32,32))
        self.imagemtiro = pygame.image.load(os.path.join('Assets','carinha.png'))
        self.imagemtiro = pygame.transform.scale(self.imagemtiro,(16,16))
        self.tiro = Tiro(0,0,0,0)
        self.tirox = 0
        self.tiroy = 1

    def move(self):
        if self.ISdead == False:
            difx = self.player.rect.x - self.rect.x
            dify = self.player.rect.y - self.rect.y

            if self.time < 0:
                self.time = 60
                if difx > 0:
                    self.tirox = 1
                    self.tiroy=0
                    self.rect.x += 32
                    if self.secolidiu() == True:
                        self.rect.x -=32 
                if difx < 0:
                    self.tirox = -1
                    self.tiroy = 0
                    self.rect.x -= 32
                    if self.secolidiu() == True:
                        self.rect.x +=32 
                if dify > 0:
                    self.tiroy = 1
                    self.tirox = 0
                    self.rect.y += 32
                    if self.secolidiu() == True:
                        self.rect.y -=32 
                if dify < 0:
                    self.tiroy = -1
                    self.tirox = 0
                    self.rect.y -= 32
                    if self.secolidiu() == True:
                        self.rect.y +=32 
            self.time -=1
            self.delay += 1   
            if self.delay > 90:
                self.tiro = Tiro(self.rect.x,self.rect.y,self.tirox,self.tiroy)
                self.delay = 0
        

    def draw(self,display):
        display.blit(self.image,(self.rect.x,self.rect.y))    
        self.tiro.movetiro(display)

class Tiro (pygame.sprite.Sprite):  
   def __init__(self,posx,posy,linha=0,coluna=0):
        super().__init__()   
        self.linha = linha 
        self.coluna = coluna
        self.imagemtiro = pygame.image.load(os.path.join('Assets','Monstros','Fireball.png'))
        self.imagemtiro = pygame.transform.scale(self.imagemtiro,(16,16))
        self.rect = self.imagemtiro.get_rect()    
        self.rect.x, self.rect.y = posx, posy+8
        self.ativo = True
   def movetiro(self,display):
        if self.ativo:
            self.rect.x += self.linha*8
            self.rect.y += self.coluna*8
            display.blit(self.imagemtiro,(self.rect.x,self.rect.y))
            if self.rect.colliderect(player.rect) and self.ativo == True:
                player.tomaDano(1)
                self.ativo = False
            