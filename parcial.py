import pygame
import sys
from personaje import *
from ahorcado import *
from funciones import *
from colores import *

# Inicializar Pygame
pygame.init()
archivo = "archivo_palabras.txt"

# Crear pantalla
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("El Ahorcado by LosTresMosqueteros")

# ICONO
icono = pygame.image.load("assets/icono.png")
pygame.display.set_icon(icono)

# FUENTE
FUENTE_TITULO = pygame.font.SysFont(None, 48, bold = True)
FUENTE_NORMAL = pygame.font.SysFont(None, 36)

#FOTOGRAMAS
RELOJ = pygame.time.Clock()

letras_presionadas = []

lista_palabras = cargar_palabras(archivo)

palabra_random = elegir_palabra(lista_palabras)

errores = 0
mensaje = "hola"

DURACION_MSJ = 3000

# Cargar personaje (usá tu imagen, por ejemplo: "personaje.png")
personaje = crear_personaje(x = 200, y= 450)
ahorcado = crear_ahorcado(x = 8, y = 80)
boton_jugar = boton(x= 275,y= 410, ruta ="assets/boton_empezar.png")

# Bucle principal
ejecutando = True
estado_jugar = False

while ejecutando:

    tiempo_actual = pygame.time.get_ticks()

    letra = ""
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if evento.unicode.isalpha():
                letra = evento.unicode.upper()
            if evento.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    if estado_jugar:
        jugar(evento, letra, palabra_random, letras_presionadas, DURACION_MSJ, personaje, ahorcado, ANCHO, pantalla, fuente = FUENTE_NORMAL, mensaje = mensaje)
    else:
        main_texto(pantalla = pantalla, fuente_titulo = FUENTE_TITULO, fuente_normal = FUENTE_NORMAL)
        if dibujo_boton(boton_jugar, pantalla):
            estado_jugar = True

    pygame.display.flip()
    pygame.display.update()
    pantalla.fill(COLOR_FONDO)
    RELOJ.tick(30)

pygame.quit()