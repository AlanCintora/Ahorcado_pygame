import pygame
import sys
from personaje import *
from ahorcado import *
from textos_juego import *

# Inicializar Pygame
pygame.init()

# Crear pantalla
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("El Ahorcado by LosTresMosqueteros")

#
RELOJ = pygame.time.Clock()

# Colores
BLANCO = (128, 128, 128)

# Cargar imagen del personaje (debe estar en el mismo directorio o indicar ruta completa)

error = 0
estado = True
estado_jugar = False
# Cargar personaje (usá tu imagen, por ejemplo: "personaje.png")
personaje = crear_personaje(x = 500, y= 10)
boton_jugar = texto(x= 300,y= 300, ruta ="assets/boton_empezar.png")

# Bucle principal
ejecutando = True
while ejecutando:

    for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False
                pygame.quit()
                sys.exit()

    if estado_jugar:
        if evento.type == pygame.KEYDOWN:
            error += 1
            if evento.key == pygame.K_ESCAPE:
                ejecutando = False

        # Movimiento con teclado
        teclas = pygame.key.get_pressed()
        movimiento(personaje, teclas, ancho_pantalla = ANCHO)

        if error == 7:
            estado = False

        # Dibujar todo
        
        dibujar_personaje(pantalla, personaje)
        dibujar_ahorcado(
                pantalla, crear_ahorcado(fallo = error, x = 400, y = 154))
    
    else:
        dibujo_textos(boton_jugar, pantalla)

    pantalla.fill(BLANCO)
    pygame.display.flip()
    pygame.display.update()
    RELOJ.tick(30)

pygame.quit()