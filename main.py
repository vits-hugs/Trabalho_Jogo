import pygame
from tiles import *
from player import player
from inimigo import Inimigo
from slime import Slime


pygame.mixer.init()

musica = pygame.mixer.Sound(os.path.join('Assets','MusicaDungeon.ogg'))
musica.play()
FPS = 60
enemy_Array = []
################################# JANELA #################################

################################ CARREGA JANELA E RELÓGIO ###################
pygame.init()
DISPLAY_W, DISPLAY_H = 900, 500
canvas = pygame.Surface((DISPLAY_W+500,DISPLAY_H+500))
window = pygame.display.set_mode(((DISPLAY_W,DISPLAY_H)))
running = True
clock = pygame.time.Clock()


################################# LOAD PLAYER ###################################
################################ CARREGA JOGADOR ################################



#################################### LOAD THE LEVEL #######################################
################################### CARREGA O NIVEL #################################
map = TileMap('faz.csv')

#instancio o player e o inimigo nos pontos
player.rect.x,player.rect.y = map.start_x,map.start_y
for pos in map.inimigos[0]:
    enemy_Array.append(Slime(pos.x,pos.y))
for pos in map.inimigos[1]:
    enemy_Array.append(Inimigo(pos.x,pos.y))
        
        
Camera_x,Camera_y =  0,0
Cam_x = 250
Cam_y = 250
################################# GAME LOOP ##########################
while running:
    dt = clock.tick(60) * .001 * FPS
    player.ataqDelay -= 1
    ################################# CHECK PLAYER INPUT #################################
    ############################# VERIFICA INPUT DO JOGADOR ####################

    for event in pygame.event.get():
        player_pos = player.Get_pos()
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
  
    
    Cam_x += ((DISPLAY_W/2 - player.rect.x)-Cam_x)*0.05
    Cam_y +=  ((DISPLAY_H/2  -player.rect.y)-Cam_y)*0.05
    if Cam_x >0:
        Cam_x = 0
    if Cam_y > 0:
        Cam_y = 0

    
    #Camera_x,Camera_y  = 
    ################################# UPDATE/ Animate SPRITE #################################
    player.update(map.tiles,enemy_Array)
    ################################# UPDATE WINDOW AND DISPLAY #################################
    canvas.fill((0, 180, 240)) # Fills the entire screen with light blue

    # desenha numa superficie
    map.draw_map(canvas)
    player.draw(canvas)
    

    for enemy in enemy_Array:
        enemy.draw(canvas)
        enemy.move()


    #bota a superficie na telaj
    window.blit(canvas,(Cam_x,Cam_y))
    window.blit(player.vidaHUD[player.vida - 1],(0,0))
    if not enemy_Array :
        print('YO WIN')

    #atualiza tela
    pygame.display.update()
