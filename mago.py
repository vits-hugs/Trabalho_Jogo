import pygame
import os
from inimigo import Inimigo #Importa a classe Inimigo para herdar métodos
from player import player  #Importa o objeto player

class Mago(Inimigo): #Criada a classe Mago, que irá herdar definições da classe Inimigo
    def __init__(self,pos_x,pos_y):  # Metodo Construtor, que primeiramente recebe o parametro self, e pos_x e pos_y (posicão inicial do mago)
        super().__init__(pos_x,pos_y) #Pega o mesmo metodo construtor da classe "Superior" ( que seria o inimigo )
        pygame.mixer.init() #Para utilizar sons
        self.delay = 120 #Variável para controlar o delay nos tiros (2 segundos)
        self.vida = 2 #Atributo vida que recebe "2" como número de vidas
        self.image = pygame.image.load(os.path.join('Assets','Monstros','mago.png')) #Aqui vamos atribuir a imagem do mago
        self.image = pygame.transform.scale(self.image,(32,32)) #Atributo que vai redimencionar a imagem do Mago para caber em um tile do terreno
        self.tiro = Tiro(0,0) #Instanciando o tiro

    def move(self): #Metodo de controle do movimento do Mago e do tiro (Controla a lógica do mago)
        #Pega o atributo de posição do retangulo do player e do retangulo do Mago
        if self.ISdead == False: #Enquanto o mago estiver vivo
            difx = self.player.rect.x - self.rect.x #Variáveis que calculam a diferença da distância do jogador e do inimigo
            dify = self.player.rect.y - self.rect.y #Uma que calcula as diferenças das cordenadas x e y, horizontal e vertical respectivamente
            #Agora são colocadas as condições para o movimento do mago e do tiro
            #Resumindo, o mago irá perseguir o Player almejando as diferenças difx e dify serem 0 e juntamente vai ser definido a direção a qual tiro vai 
            if self.time < 0: 
                self.time = 60 #Variável de controlar o delay movimento
                if difx > 0: #Se a diferença das cordenadas X for maior que 0 
                    self.tirox = 1 #Posição do movimento do tiro para direita
                    self.tiroy=0 
                    self.rect.x += 32 #A posição x do retangulo do inimigo precisa aumentar em 32 (que é o tamanho de cada tile do mapa)
                    if self.secolidiu() == True: #Também dentro das condições foi adicionado uma definição herdada do inimigo
                        self.rect.x -=32  #Para negar o movimento caso haja colisão com algum retangulo do mapa
                #Então vai seguindo na mesma linha        
                if difx < 0: #Anterior era para movimentar para esquerda, esse para direita
                    self.tirox = -1 #Posição do momimento do tiro para esquerda
                    self.tiroy = 0
                    self.rect.x -= 32
                    if self.secolidiu() == True:
                        self.rect.x +=32 
                if dify > 0: #Para baixo
                    self.tiroy = 1 #Posição do momimento do tiro para baixo
                    self.tirox = 0
                    self.rect.y += 32
                    if self.secolidiu() == True:
                        self.rect.y -=32 
                if dify < 0: #Para cima
                    self.tiroy = -1 #Posição do momimento do tiro para cima
                    self.tirox = 0
                    self.rect.y -= 32
                    if self.secolidiu() == True:
                        self.rect.y +=32 

            self.time -= 1 #Diminuição do delay do movimento

            if self.delay < 0: #Booleano para controlar o delay do tiro
                self.delay = 120
                self.tiro = Tiro(self.rect.x,self.rect.y,self.tirox,self.tiroy) #Instancia um novo tiro baseado na posição Mago
            self.delay -= 1  #Diminuição do delay do tiro
        

    def draw(self,display): #Metodo de desenhar os objetos
        display.blit(self.image,(self.rect.x,self.rect.y)) #Função que desenha o player na tela
        self.tiro.movetiro(display) #Função que desenha o tiro na tela

class Tiro (pygame.sprite.Sprite): #Classe tiro 
   def __init__(self,posx,posy,linha=0,coluna=0): #Método Construtor, que define a posição e a direção  
        self.linha = linha #Função Velocidade horizontal do tiro 
        self.coluna = coluna #Função Velocidade vertical do tiro 
        self.imagemtiro = pygame.image.load(os.path.join('Assets','Monstros','Fireball.png')) #Aqui vamos atribuir a imagem do tiro
        self.imagemtiro = pygame.transform.scale(self.imagemtiro,(16,16)) #Atributo que vai redimencionar a imagem do tiro para caber em um quarto do tile do terreno
        self.rect = self.imagemtiro.get_rect()  #Função para calcular o retangulo da imagemtiro  
        self.rect.x, self.rect.y = posx, posy+8 #Faz a posição do tiro no meio do mago
        self.ativo = True

   def movetiro(self,display): #Metodo que vai mover o tiro
        if self.ativo: #O tiro começa ativo
            self.rect.x += self.linha*8 #O que realmente movimenta o tiro
            self.rect.y += self.coluna*8
            display.blit(self.imagemtiro,(self.rect.x,self.rect.y))
            if self.rect.colliderect(player.rect) and self.ativo == True:  #Se atingir o player ele toma dano e self.ativo é inativado
                player.tomaDano(1) #Chama o metodo tomaDano do ojeto player
                self.ativo = False 
            