import pygame
from tiles import *
from player import player
from inimigo import Inimigo
from slime import Slime

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
            self.enemy_Array.append(Inimigo(pos.x,pos.y))
        pygame.mixer.init()

        musica = pygame.mixer.Sound(os.path.join('Assets','MusicaDungeon.ogg'))
        musica.play()


    def Game(self):
       
        player.ataqDelay -= 1
        ################################# CHECK PLAYER INPUT #################################
        ############################# VERIFICA INPUT DO JOGADOR ####################
        running = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
            #se tecla foi apertada
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: #verifica q tecla foi
                    player.LEFT_KEY = True
                # Camera_x += 32
                elif event.key == pygame.K_RIGHT: 
                    player.RIGHT_KEY = True
                    #Camera_x -= 32
                elif event.key == pygame.K_DOWN:
                    player.DOWN_KEY = True
                # Camera_y -= 32
                elif event.key == pygame.K_UP:
                    player.UP_KEY = True
                # Camera_y += 32
                if event.key == pygame.K_j:
                    if player.ataqDelay <= 0:
                        player.ataq = True
                        player.ataqDelay = 30
            
                    

            
        ## Camera
    
        
        self.cam.x += ((self.Display_W/2 - player.rect.x)-self.cam.x)*0.05
        self.cam.y +=  ((self.Display_H/2  -player.rect.y)-self.cam.y)*0.05
        if self.cam.x >0:
            self.cam.x = 0
        if self.cam.y > 0:
            self.cam.y = 0

        
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


        #bota a superficie na telaj
        self.window.blit(self.canvas,(self.cam.x,self.cam.y))
        self.window.blit(player.vidaHUD[player.vida - 1],(0,0))
        if not self.enemy_Array :
            self.fase = self.Fases[self.nivelCount]
            self.nivelCount +=1
            return False

        #atualiza tela
        pygame.display.update()
        return running