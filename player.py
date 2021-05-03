import pygame
import os
import inimigo
#Criei classe player
class Player(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):#Valores quando o player for iniciado
        pygame.sprite.Sprite.__init__(self)#inicia como sprite
        pygame.mixer.init()
        #Carrega imagem e da uma retangulo pra ela
        self.image = pygame.image.load(os.path.join('Assets','Jogador','player.png'))
        self.image = pygame.transform.scale(self.image,(32,32))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x 
        self.rect.y = pos_y 
        self.tomadano = pygame.mixer.Sound(os.path.join('Assets','Jogador','Nah.wav'))

        self.ataqX = 1
        self.ataqY = 0
        self.ataq = False
        self.ataq_img = pygame.image.load(os.path.join('Assets','Jogador','Ataq.png'))
        self.ataqPos = pygame.math.Vector2(0,0)
        self.ataqDelay = 0
        self.delay =0
        self.som = pygame.mixer.Sound(os.path.join('Assets','Jogador','Espada.wav'))

        #verific inputs
        self.LEFT_KEY, self.RIGHT_KEY ,self.UP_KEY ,self.DOWN_KEY = False,False,False,False
    
        #posição X e Y
        self.position = pygame.math.Vector2(0, 0)
        

        #troca as imagens
        self.R_image = pygame.image.load(os.path.join('Assets','Jogador','Idle_R.png'))
        self.L_image = pygame.image.load(os.path.join('Assets','Jogador','Idle_L.png'))
        self.Up_image = pygame.image.load(os.path.join('Assets','Jogador','Idle_Up.png'))
        self.D_image = pygame.image.load(os.path.join('Assets','Jogador','Idle_D.png'))
        
        #deixa elas no tamanho certo
        self.R_image = pygame.transform.scale(self.R_image,(32,32))
        self.L_image = pygame.transform.scale(self.L_image,(32,32))
        self.Up_image = pygame.transform.scale(self.Up_image,(32,32))
        self.D_image = pygame.transform.scale(self.D_image,(32,32))

        #STATUS
        self.VEL = 32 #velocidade

        self.vidaHUD = [pygame.image.load(os.path.join('Assets','Jogador','Vida1.png')),pygame.image.load(os.path.join('Assets','Jogador','Vida2.png')),pygame.image.load(os.path.join('Assets','Jogador','VidaCheia.png'))]
        self.vida = 3 #vida
        self.IsVivo = True
    
    def tomaDano(self,dano):
        if self.vida > 0:
            self.tomadano.play()
            self.vida-= dano
        if self.vida <= 0: 
            self.vida = 0
            self.image = pygame.image.load(os.path.join('Assets','Monstros','novomorre.png'))
            self.IsVivo = False
        
    #desenha player na tela
    def draw(self,display):
        
        display.blit(self.image,(self.rect.x,self.rect.y))
        
        if self.ataqDelay > 0:
            display.blit(self.ataq_img,self.ataqPos)
         
        
            
    
  
    def update(self,tiles,lista_de_Inimigo):
        self.tiles = tiles
        if self.LEFT_KEY == True:# se setinha pra esquerda foi pressionada
            #troca imagem
            self.image = self.L_image

            self.ataqX = -1#define o ataque pra esquerda
            self.ataqY = 0

            self.rect.x -=self.VEL #move
           

            self.LEFT_KEY = False
            if self.coli(tiles) == True or self.coli(lista_de_Inimigo):  #se houver colisão ele volta
                self.rect.x += self.VEL
            


        elif self.RIGHT_KEY== True:
            self.image = self.R_image

            self.ataqX = 1
            self.ataqY = 0


            self.rect.x += self.VEL
            
            self.RIGHT_KEY=False
            if self.coli(tiles) == True or self.coli(lista_de_Inimigo):
                self.rect.x -= self.VEL

        elif self.UP_KEY== True:
            self.image = self.Up_image

            
            self.ataqX = 0
            self.ataqY = -1

            self.rect.y -=self.VEL
            self.UP_KEY =False
            if self.coli(tiles) == True or self.coli(lista_de_Inimigo):
                self.rect.y += self.VEL

        elif self.DOWN_KEY== True:
            self.image = self.D_image

            self.ataqX = 0
            self.ataqY = 1

            self.rect.y +=self.VEL
            self.DOWN_KEY = False
            if self.coli(tiles) == True or self.coli(lista_de_Inimigo):
                self.rect.y -= self.VEL
        
        elif self.ataq == True:
            self.Ataque(lista_de_Inimigo)
            self.ataq = False
            
            
            

    def Ataque(self,lista_de_Inimigo):
        self.som.play()
        self.ataqPos = pygame.math.Vector2(self.rect.x+(32*self.ataqX),self.rect.y+(32*self.ataqY))
        for enemy in lista_de_Inimigo:
            if pygame.Rect.collidepoint(enemy.rect,self.ataqPos) == True:
                
                if enemy.ISdead:
                    lista_de_Inimigo.remove(enemy)
                enemy.tomarDano(1)
        self.ataq = False
            


                


    def coli(self,tiles):
        for tile in tiles:
            if self.rect.colliderect(tile):
                return(True)

    #def Get_pos(self):
     #   playerPos = pygame.math.Vector2(self.rect.x,self.rect.y)
      #  return playerPos

player = Player(0,0)