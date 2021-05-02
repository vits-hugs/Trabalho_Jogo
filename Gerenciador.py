import pygame
from tiles import *
from player import player
from inimigo import Inimigo
from slime import Slime
from mago import mago
class Gerenciador():
    def __init__(self,player):
        self.nivelCount = 0
        self.Fases = ['test_level.csv','Fase_2.csv']


        self.player = player
        self.cam = pygame.math.Vector2(0,0)
    
        self.Display_W, self.Display_H = 900, 500

        self.fase = 'faz.csv'

        self.enemy_Array = []
    def Faz_mapa(self,window,canvas):
        self.window = window
        self.canvas = canvas
    
        self.map = TileMap(self.fase)
    
        player.rect.x,player.rect.y = self.map.start_x,self.map.start_y
        for pos in self.map.inimigos[0]:
            self.enemy_Array.append(Slime(pos.x,pos.y))
        for pos in self.map.inimigos[1]:
            self.enemy_Array.append(mago(pos.x,pos.y))
        pygame.mixer.init()
        
        pygame.mixer.music.load(os.path.join('Assets','MusicaDungeon.ogg'))

        pygame.mixer.music.play()


    def Game(self):
       

        
        self.cam.x += ((self.Display_W/2 - player.rect.x)-self.cam.x)*0.05
        self.cam.y +=  ((self.Display_H/2  -player.rect.y)-self.cam.y)*0.05
        if self.cam.x >0:
            self.cam.x = 0
        if self.cam.y > 0:
            self.cam.y = 0

        if self.cam.x < -1*(self.Display_W/2)+13*32 :
            self.cam.x = -1*(self.Display_W/2)+13*32 
        if self.cam.y < -(self.Display_H/2)+4*32 :
            self.cam.y = -(self.Display_H/2)+4*32 
        


        
        #Camera_x,Camera_y  = 
        ################################# UPDATE/ Animate SPRITE #################################
        player.update(self.map.tiles,self.enemy_Array)
        ################################# UPDATE self.window AND DISPLAY #################################
       

        # desenha numa superficie
        self.map.draw_map(self.canvas)
        player.draw(self.canvas)
        for enemy in self.enemy_Array:
            enemy.draw(self.canvas)
            enemy.move()
        
         
        if player.ataqDelay > 0:
            self.canvas.blit(player.ataq_img,player.ataqPos)
         
       

        #bota a superficie na telaj
        self.window.blit(self.canvas,(self.cam.x,self.cam.y))
        self.window.blit(player.vidaHUD[player.vida - 1],(0,0))
        if not self.enemy_Array :
            self.fase = self.Fases[self.nivelCount]
            self.nivelCount +=1
            return False

        #atualiza tela
        pygame.display.update()
        return True
