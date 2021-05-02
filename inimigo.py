import pygame
import os
from player import player

#Criei classe inimigo
class Inimigo(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):#Valores quando o inimigo for iniciado
        pygame.sprite.Sprite.__init__(self)#inicia como sprite
        
        self.delay = 60

       

        self.player = player
        
        #Carrega imagem e da uma retangulo pra ela
        self.image = pygame.image.load(os.path.join('Assets','Monstros','zombie_idle_anim_f0.png'))
        self.image = pygame.transform.scale(self.image,(32,32))
        self.rect =self.image.get_rect()
        self.rect.x,self.rect.y = pos_x,pos_y

        self.time = 0

        self.morreu = pygame.image.load(os.path.join('Assets','Monstros','novomorre.png'))
        self.ISdead = False


        self.vida = 1




    def tomarDano(self,dano):
        self.vida -= dano
        if self.vida <= 0:
            self.image = self.morreu
            self.ISdead = True
         
          
            
    #desenhar na tela
    def draw(self,display):
        display.blit(self.image,(self.rect.x,self.rect.y))
    
    def move(self):

        if self.time < 0:
            self.rect.x += 32
            self.time = 60
        self.time -=1
    def Dardano(self,dano):
        player.vida -= dano
    def secolidiu(self):
        if self.rect.colliderect(player):
            return(True)
        for tile in player.tiles:
            if self.rect.colliderect(tile):
                return(True)
        
    
        
        
