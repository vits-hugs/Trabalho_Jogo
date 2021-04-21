import pygame
from tiles import *
from player import player
from inimigo import Inimigo
from slime import Slime
from Gerenciador import Gerenciador



FPS = 60


pygame.init()
DISPLAY_W, DISPLAY_H = 900, 500
canvas = pygame.Surface((DISPLAY_W+500,DISPLAY_H+500))
window = pygame.display.set_mode(((DISPLAY_W,DISPLAY_H)))


running = True
Grc = Gerenciador(player)

while running:
    
    clock = pygame.time.Clock()
   
    Grc.Faz_mapa(window,canvas)  
    infaze = True
    ################################# GAME LOOP ##########################
    while infaze:
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
        
        dt = clock.tick(60) * .001 * FPS
        infaze = Grc.Game()
        
        