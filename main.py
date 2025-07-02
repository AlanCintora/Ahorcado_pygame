# Importamos las librerías necesarias
import pygame


# Inicializamos Pygame
pygame.init()
pygame.mixer.init()

# Dimensiones de la ventana
ANCHO = 800
ALTO = 600

# Ícono
icono = pygame.image.load("assets\icono.png")
pygame.display.set_icon(icono)

# Creamos la ventana principal
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Ahorcado by 3 mosqueteros")

# Colores (RGB)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
NEGRO = (0, 0, 0)
COLOR_FONDO = (220, 220, 255)

# Fuente para los textos
FUENTE = pygame.font.SysFont(None, 48)

# Cargamos el sonido de error
sonido_error = pygame.mixer.Sound("assets\error.wav")

# Cargamos musica de background 
pygame.mixer.music.load("assets\suspense_background.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3) 

#######Funciones para testing#################
#Función para mostrar texto en pantalla
def mostrar_texto(texto, x, y):
    superficie = FUENTE.render(texto, True, NEGRO)
    ventana.blit(superficie, (x, y))

# Función para dibujar cruces rojas por cada error cometido
def dibujar_cruces(errores):
    for i in range(errores):
        # Cada cruz se desplaza 50 píxeles hacia la derecha
        x = 50 + i * 60
        y = 50
        pygame.draw.line(ventana, ROJO, (x, y), (x + 30, y + 30), 5)
        pygame.draw.line(ventana, ROJO, (x + 30, y), (x, y + 30), 5)

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

    pygame.mixer.music.load("assets\suspense_background.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.3) 

    while jugando:
        ventana.fill(COLOR_FONDO) 
        
        # Mostrar breve explicacion
        mostrar_texto("Ahorcado - ¡Adivina la palabra o serás colgado!", 20, 300)
        mostrar_texto(f"Intentos: {intentos}", 50, 550)


        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
               jugando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
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
