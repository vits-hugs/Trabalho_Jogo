 
import pygame
pygame.init()
DISPLAY_W, DISPLAY_H = 900, 500
canvas = pygame.Surface((DISPLAY_W+500,DISPLAY_H+500))
window = pygame.display.set_mode(((DISPLAY_W,DISPLAY_H)))
running = True 
while running: 
  for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    