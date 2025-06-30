import pygame

pygame.init()

ANCHO = 800
ALTO = 600


pantalla = pygame.display.set_mode((ANCHO,ALTO))

pygame.display.set_caption("Ahorcado")

logo_juego = pygame.image.load("Segundo_Parcial\\ahorcado.png")
pygame.display.set_icon(logo_juego)

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    pantalla.fill((0,55,0))
    
    pygame.display.update()