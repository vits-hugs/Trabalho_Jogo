import pygame
from tiles import *
from player import player
from inimigo import Inimigo
from slime import Slime
from Gerenciador import Gerenciador



FPS = 60

    ################################# JANELA #################################

    ################################ CARREGA JANELA E RELÓGIO ###################
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
        dt = clock.tick(60) * .001 * FPS
        infaze = Grc.Game()
        print(Grc.fase)