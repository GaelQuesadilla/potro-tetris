import pygame
import sys
"""from src.model.Tetromino import FiguraRandom"""
import random

pygame.init()

ancho , alto = 10,20
titulo= 45
game_res= ancho* titulo, alto*titulo
fps=60

"""figuras = FiguraRandom()"""

game_sc = pygame.display.set_mode(game_res)
pygame.display.set_caption("Tetris")
reloj= pygame.time.Clock()

cuadricula = [pygame.Rect(x*titulo, y*titulo, titulo, titulo) for x in range (ancho) for y in range (alto)]

while True:
   
    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            pygame.quit()
            sys.exit()
    game_sc.fill(pygame.Color("black") )

    [pygame.draw.rect(game_sc, (40,40,40), i_rect, 1) for i_rect in cuadricula]

    pygame.display.flip()
    reloj.tick(fps)


