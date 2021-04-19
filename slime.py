from inimigo import Inimigo
import os,pygame
class Slime(Inimigo):
    def __init__(self,pos_x,pos_y):
        super().__init__(pos_x,pos_y)
        pygame.mixer.init()
        self.vida = 3
        self.image = pygame.image.load(os.path.join('Assets','Monstros','slime.png'))
        self.morreu = pygame.image.load(os.path.join('Assets','Monstros','SlimeMorto.png'))
        self.idle = pygame.image.load(os.path.join('Assets','Monstros','slime.png'))

     

        self.som = pygame.mixer.Sound(os.path.join('Assets','Monstros','Nah.wav'))


        self.ataq_img = pygame.image.load(os.path.join('Assets','Monstros','SlimeMorto.png'))
        self.Atacou = False
        self.delay = 0
        self.puto = pygame.image.load(os.path.join('Assets','Monstros','Brabo.png'))



        self.ISputo = False
        self.impaciencia =0

    def draw(self,display):
        display.blit(self.image,(self.rect.x,self.rect.y))    
        if self.Atacou == True and self.delay > 0:
            display.blit(self.ataq_img,(self.player.rect.x,self.player.rect.y))
            self.delay -= 1
    def move(self):
        if self.ISdead == False:
            dx = self.player.rect.x - self.rect.x 
            dy = self.player.rect.y - self.rect.y
           
            if dx ==32 or -dx  == 32:
                if dy == 0:
                    self.ISputo = True
                else:
                    self.ISputo = False   
                
            elif dy ==32 or -dy  == 32:
                if dx == 0:
                    self.ISputo = True
                else:
                    self.ISputo = False   
            else:
                self.ISputo = False

            if self.ISputo:
                self.Atacou = True
                self.image = self.puto
                self.impaciencia += 1
                if self.impaciencia >=45:
                    self.som.play()
                    self.delay =15
                    self.player.tomaDano(1)
                    self.impaciencia = 0
            else:
                self.image = self.idle
                self.impaciencia = 0
            
                
                self.time +=1
                if self.time == 0:
                    self.rect.x += 32
                elif self.time == 60:
                    self.rect.y += 32
                elif self.time == 120:
                    self.rect.x -= 32
                elif self.time == 180:
                    self.rect.y -= 32
                    self.time = -60
     
algo = pygame.image.load(os.path.join('Assets','Monstros','novomorre.png'))
                
            
            
            
            
            