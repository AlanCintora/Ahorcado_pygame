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

# ICONO
icono = pygame.image.load("assets/icono.png")
pygame.display.set_icon(icono)

# FUENTE
FUENTE = pygame.font.SysFont(None, 48)

#FOTOGRAMAS
RELOJ = pygame.time.Clock()

# Colores
BLANCO = (128, 128, 128)
NEGRO = (0, 0, 0)

# Cargar imagen del personaje (debe estar en el mismo directorio o indicar ruta completa)

error = 0
estado_jugar = False
# Cargar personaje (usá tu imagen, por ejemplo: "personaje.png")
personaje = crear_personaje(x = 200, y= 200)
boton_jugar = boton(x= 150,y= 150, ruta ="assets/boton_empezar.png")

# Bucle principal
ejecutando = True
while ejecutando:

    for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False
                sys.exit()

    if estado_jugar:
        teclas = pygame.key.get_pressed()
        if evento.type == pygame.KEYDOWN:
            error += 1
            if evento.key == pygame.K_ESCAPE:
                ejecutando = False

        # Movimiento con teclado
        movimiento(personaje, teclas, ancho_pantalla = ANCHO)

        if error == 7:
            error = 0

        # Dibujar todo
        dibujar_personaje(pantalla, personaje)
        dibujar_ahorcado(
                pantalla, crear_ahorcado(fallo = error, x = 400, y = 154))
    else:
        mostrar_texto(FUENTE, NEGRO, "Ahorcado - ¡Adivina la palabra o seras colgado!", 0, 0, pantalla)
        if dibujo_textos(boton_jugar, pantalla):
             estado_jugar = True

    pygame.display.update()
    pygame.display.flip()
    pantalla.fill(BLANCO)
    RELOJ.tick(30)

pygame.quit()
