import pygame
from tiles import *
from player import player
from inimigo import Inimigo
from slime import Slime

#inicia o mixer
pygame.mixer.init()
musica = pygame.mixer.Sound(os.path.join('Assets','MusicaDungeon.ogg'))
musica.play()

#Seta FPS
FPS = 60
#Onde os inimigos ficam guardadinhos 
enemy_Array = []

################################# JANELA #################################

################################ CARREGA JANELA E RELÓGIO ###################
pygame.init()

map = TileMap('faz.csv')
DISPLAY_W, DISPLAY_H = 900, 500#tamanho da janela
canvas = pygame.Surface((map.map_w,map.map_h))#tamanho do nivel
window = pygame.display.set_mode(((DISPLAY_W,DISPLAY_H)))#janela sendo feita


#################################### LOAD THE LEVEL #######################################
################################### CARREGA O NIVEL #################################

#map = TileMap('faz.csv') #Gera o mapa ver em tiles.py

#instancio o player e o inimigo nos pontos
player.rect.x,player.rect.y = map.start_x,map.start_y #mapa define posição inicial do player

for pos in map.inimigos[0]:                 #pega as posições que o mapa cria e coloca 
    enemy_Array.append(Slime(pos.x,pos.y)) #os respectivos inimigos
for pos in map.inimigos[1]:
    enemy_Array.append(Inimigo(pos.x,pos.y))
        
        

Cam_x = 250         
Cam_y = 250


running = True #loop que define quando o jogo ta rodando
clock = pygame.time.Clock() #variavel de controle do clock
################################# GAME LOOP ##########################
while running:
    dt = clock.tick(60) * .001 * FPS #variação de tempo não usei direito ainda

    player.ataqDelay -= 1 # jogador delay do ataque ta sempre baixando
    ################################# CHECK PLAYER INPUT #################################
    ############################# VERIFICA INPUT DO JOGADOR ####################

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
   
        #se tecla foi apertada
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: #verifica q tecla foi
                player.LEFT_KEY = True

            elif event.key == pygame.K_RIGHT: 
                player.RIGHT_KEY = True
    
            elif event.key == pygame.K_DOWN:
                player.DOWN_KEY = True
              
            elif event.key == pygame.K_UP:
                player.UP_KEY = True
          
            if event.key == pygame.K_j:
                if player.ataqDelay <= 0:
                    player.ataq = True
                    player.ataqDelay = 30
        
                

          
    ## Camera
  
    #camera segue 
    Cam_x += ((DISPLAY_W/2 - player.rect.x)-Cam_x)*0.05
    Cam_y +=  ((DISPLAY_H/2  -player.rect.y)-Cam_y)*0.05
    #impede a camera de sair do mapa gerado 
    if Cam_x >0:
        Cam_x = 0
    if Cam_y > 0:
        Cam_y = 0
    if Cam_x < -62:
        Cam_x = -62
    if Cam_y < -134:
        Cam_y = -134

    
   
    ################################# UPDATE/ Animate SPRITE #################################
    player.update(map.tiles,enemy_Array)
    ################################# UPDATE WINDOW AND DISPLAY #################################
    
    
    # desenha numa superficie
    map.draw_map(canvas) #desenha o mapa num canvas
    player.draw(canvas)
    

    for enemy in enemy_Array:
        enemy.draw(canvas)
        enemy.move()


    #bota a superficie na telaj
    window.blit(canvas,(Cam_x,Cam_y)) #depos desenha o canvas na tela
    #window.blit(player.vidaHUD[player.vida - 1],(0,0))
    if not enemy_Array :
        print('YO WIN')


    

    pygame.display.update() #atualiza a tela
