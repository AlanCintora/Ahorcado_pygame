import pygame
import sys
from personaje import *
from ahorcado import *
from funciones_facundo import *
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
FUENTE = pygame.font.SysFont(None, 48)

#FOTOGRAMAS
RELOJ = pygame.time.Clock()

# Cargar imagen del personaje (debe estar en el mismo directorio o indicar ruta completa)
errores = 0

letras_presionadas = []

lista_palabras = cargar_palabras(archivo)

palabra_random = elegir_palabra(lista_palabras)
    
mensaje = ""
letra = ""
tiempo_mensaje = 0
DURACION_MENSAJE = 1000

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
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            letra = evento.unicode.upper()

    if estado_jugar:
        jugar(evento, letra, palabra_random, letras_presionadas, DURACION_MENSAJE, personaje, ANCHO, pantalla, fuente = FUENTE, mensaje = mensaje, errores= errores)
    else:
        mostrar_texto(FUENTE, NEGRO, "Ahorcado - ¡Adivina la palabra o seras colgado!", 0, 0, pantalla)
        if dibujo_textos(boton_jugar, pantalla):
            estado_jugar = True

    pygame.display.flip()
    pygame.display.update()
    pantalla.fill(COLOR_FONDO)
    RELOJ.tick(30)

pygame.quit()