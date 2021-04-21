import pygame
import os
from inimigo import Inimigo
#Downloads\JogoTop-master\JogoTop-master

class mago(Inimigo):
    def __init__(self,pos_x,pos_y):
        super().__init__(pos_x,pos_y)
        pygame.mixer.init()
        self.vida = 2
        self.image = pygame.image.load(os.path.join('Assets','Monstros','mago.jpg'))
        self.image = pygame.transform.scale(self.image,(32,32))
        self.imagemtiro = pygame.image.load(os.path.join('Assets','carinha.png'))
        self.imagemtiro = pygame.transform.scale(self.imagemtiro,(16,16))

    def move(self):
        difx = self.player.rect.x - self.rect.x
        dify = self.player.rect.y - self.rect.y

        if self.time < 0:
            self.time = 60
            if difx > 0:
                self.rect.x += 32
                if self.secolidiu() == True:
                    self.rect.x -=32 
            if difx < 0:
                self.rect.x -= 32
                if self.secolidiu() == True:
                   self.rect.x +=32 
            if dify > 0:
                self.rect.y += 32
                if self.secolidiu() == True:
                   self.rect.y -=32 
            if dify < 0:
                self.rect.y -= 32
                if self.secolidiu() == True:
                   self.rect.y +=32 
        self.time -=1
    
    def draw(self,display):
        display.blit(self.image,(self.rect.x,self.rect.y))    
        self.tiro(display)
    
    def tiro(self,display):
        display.blit(self.imagemtiro,(self.rect.x//2,self.rect.y))
    

class Tiro ():  
   def __init__(self,postirox,postiroy):
        self.imagemtiro = pygame.image.load(os.path.join('Assets','carinha.png'))
        self.imagemtiro = pygame.transform.scale(self.imagemtiro,(16,16))
        self.rect = self.imagemtiro.get_rect()    
    
    
        

