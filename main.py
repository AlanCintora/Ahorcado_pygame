# Importamos las librerías necesarias
import pygame


# Inicializamos Pygame
pygame.init()
pygame.mixer.init()

# Dimensiones de la ventana
ANCHO = 800
ALTO = 600

# Ícono
icono = pygame.image.load("icono.png")
pygame.display.set_icon(icono)

# Creamos la ventana principal
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Ahorcado by 3 mosqueteros")

# Colores (RGB)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
NEGRO = (0, 0, 0)

# Fuente para los textos
FUENTE = pygame.font.SysFont(None, 48)

# Cargamos el sonido de error
sonido_error = pygame.mixer.Sound("error.wav")

#######Funciones para testing#################
#Función para mostrar texto en pantalla
def mostrar_texto(texto, x, y):
    superficie = FUENTE.render(texto, True, NEGRO)
    ventana.blit(superficie, (x, y))

# Función que inicia un nuevo juego, devolviendo estructuras iniciales
def nuevo_juego():
    intentos = []  # Lista vacía para registrar intentos
    errores = 0    # Contador de errores
    return intentos, errores

# ----------------- BUCLE PRINCIPAL -----------------
def jugar():
    # 1. Cargar palabras desde archivo y elegir una al azar
    # 2. Inicializar estructuras necesarias: letras_adivinadas, errores, reloj, banderas
    reloj = pygame.time.Clock()  # Controla la velocidad del juego
    jugando = True
    intentos, errores = nuevo_juego()

    while jugando:
        ventana.fill(BLANCO) 
        
        # Mostrar breve explicacion
        mostrar_texto("Ahorcado - ¡Adivina la palabra o serás colgado!", 20, 300)
        mostrar_texto(f"Intentos: {intentos}", 50, 550)


        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
               jugando = False
            elif evento.type == pygame.KEYDOWN:
                 if pygame.K_ESCAPE:
                     jugando = False
            
        pygame.display.update()
        pygame.display.flip()
        reloj.tick(30)

    # Cerramos Pygame correctamente
    pygame.quit()
    # Instrucción: este bloque debe ser completado por el estudiante según las consignas
    pass

# No ejecutar el juego automáticamente: solo se invoca desde consola o importación
# Descomentar la línea siguiente para probar el juego terminado:
jugar()
