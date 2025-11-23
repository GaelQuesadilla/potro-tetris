import pygame
import sys

pygame.init()

ancho , alto = 10,20
titulo= 45
game_res= ancho* titulo, alto*titulo
res = 750,940
fps=60

sc = pygame.display.set_mode(res)
game_sc = pygame.Surface(game_res)
pygame.display.set_caption("Tetris")
reloj= pygame.time.Clock()

cuadricula = [pygame.Rect(x *titulo, y*titulo, titulo, titulo) for x in range (ancho) for y in range (alto)]

#Fondo y fuente
fodo_principal = pygame.Surface(res)
fodo_principal.fill((30,30,50))
fuente_titulo = pygame.font.SysFont('tetrominoes.ttf', 75, bold = True)
fuente_texto = pygame.font.SysFont('tetrominoes.ttf', 40, bold = True)
titulo_texto = fuente_titulo.render ("TETRIS", True, (255,255,255))
titulo_sombra = fuente_titulo.render ("TETRIS", True, (100,100,100))


while True:
    sc.blit(fodo_principal, (0,0))
    sc.blit(game_sc, (20,20))
    game_sc.fill(pygame.Color("black"))

    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            pygame.quit()
            sys.exit()

    game_sc.fill(pygame.Color("black"))

    [pygame.draw.rect(game_sc, (40,40,40), i_rect, 1) for i_rect in cuadricula]

    sc.blit(titulo_sombra, (515,12))
    sc.blit(titulo_texto, (513,10))

    txt_pieza_sig= fuente_texto.render("Pieza siguiente",True, (255,255,255))
    sc.blit(txt_pieza_sig, (510,150))
    texto_puntuacion = fuente_texto.render ("Puntuacion: 0", True, (255,255,255))
    sc.blit(texto_puntuacion, (510,850))


    pygame.display.flip()
    reloj.tick(fps)


