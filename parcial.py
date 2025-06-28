import pygame
from personaje import *
from ahorcado import *

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
# Cargar personaje (usá tu imagen, por ejemplo: "personaje.png")
personaje = crear_personaje(x = 500, y= 10)

# Bucle principal
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        if evento.type == pygame.KEYDOWN:
            error += 1
            if evento.key == pygame.K_ESCAPE:
                ejecutando = False

    # Movimiento con teclado
    teclas = pygame.key.get_pressed()
    movimiento(personaje, teclas, ancho_pantalla = ANCHO)

    if error == 7:
        error = 0

    # Dibujar todo
    pantalla.fill(BLANCO)
    dibujar_personaje(pantalla, personaje)
    dibujar_ahorcado(
        pantalla, crear_ahorcado(fallo = error, x = 400, y = 154))
    pygame.display.update()
    RELOJ.tick(30)

pygame.quit()