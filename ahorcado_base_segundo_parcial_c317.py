# === PROYECTO FINAL - JUEGO DEL AHORCADO EN PYGAME ===
# Instrucciones:
# - Usar funciones, listas, diccionarios y archivos.
# - No usar clases ni programación orientada a objetos.
# - El juego debe leer palabras desde un archivo de texto externo (palabras.txt).
# - Mostrar la palabra oculta en pantalla, los intentos y las letras ingresadas.
# - Dibujar el muñeco del ahorcado a medida que se cometen errores (cabeza, cuerpo, brazos, piernas).
# - Mostrar mensaje final al ganar o perder.
# - Organizar el código con funciones bien nombradas.
# - El código debe estar comentado línea por línea.
# - Solo las partes del cuerpo deben contar como errores, no el soporte del ahorcado.


import pygame
from personaje import *
from ahorcado import *
from colores import *
import random

archivo = "archivo_palabras.txt"











pygame.init()

# ----------------- CONFIGURACIÓN DE PANTALLA -----------------
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
#completar con nombre del equipo
pygame.display.set_caption("Juego del Ahorcado")
logo_juego = pygame.image.load("imagenes\\fondo.png")
pygame.display.set_icon(logo_juego)
RELOJ = pygame.time.Clock()
FPS = 18

# ----------------- COLORES  se pueden modificar por los que elija el equipo-----------------
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)

# ----------------- FUENTE -----------------
FUENTE = pygame.font.SysFont(None, 48)

#-------------------Modelo de funciones, se deberan realizar en un archivo aparte
# Las funciones del personaje deben ser creadas y completadas por el equipo en un archivo aparte
# -------------------

# ----------------- CARGAR PALABRAS DESDE ARCHIVO -----------------
def cargar_palabras(nombre_archivo):
    # Leer las palabras desde un archivo de texto y devolver una lista
    # Asegurate de tener un archivo llamado palabras.txt con una palabra por línea
    lista_palabras = []

    try:
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            for linea in f:
                palabra = linea.strip()
                if palabra:
                    lista_palabras.append(palabra)
    except Exception as e:
        print("Error al procesar el archivo:", e)
    return lista_palabras


# ----------------- ELEGIR PALABRA AL AZAR -----------------
def elegir_palabra(lista_palabras):
    if lista_palabras:
        return random.choice(lista_palabras).upper()
    else:
        return None
        
    # Elegir una palabra aleatoria de la lista y convertirla a mayúsculas
    pass

# ----------------- DIBUJAR ESTRUCTURA DEL AHORCADO -----------------
def dibujar_estructura(pantalla, ruta, posicion=(0,0), tamaño = None):
    # Dibuja la base, palo y cuerda del ahorcado (no cuenta como error)
    imagen_base_ahorcado = pygame.image.load(ruta)
    if tamaño:
        imagen_base_ahorcado = pygame.transform.scale(imagen_base_ahorcado, tamaño)
    pantalla.blit(imagen_base_ahorcado,posicion)
    
lista_animacion_personaje = [pygame.image.load("imagenes\\1.png"),
                             pygame.image.load("imagenes\\2.png"),
                             pygame.image.load("imagenes\\3.png"),
                             pygame.image.load("imagenes\\4.png"),
                             pygame.image.load("imagenes\\5.png"),
                             pygame.image.load("imagenes\\6.png"),
                             pygame.image.load("imagenes\\7.png")]

# ----------------- DIBUJAR PARTES DEL CUERPO -----------------
def dibujar_cuerpo(errores, lista_animacion_personaje):
    # Dibujar cabeza, tronco, brazos y piernas en base a la cantidad de errores
    for i in range(errores):
        if i < len(lista_animacion_personaje):
            pantalla.blit(lista_animacion_personaje[i], (300,300))
            
            
# ----------------- DIBUJAR JUEGO EN PANTALLA -----------------
def dibujar_juego(ruta, palabra, letras_presionadas, errores,  mensaje=""):
    # Llenar fondo, mostrar palabra oculta, letras ingresadas y dibujar estructura y cuerpo
    fondo = pygame.image.load(ruta)
    
    pantalla.blit(fondo, (0,0))

    for i, letra in enumerate(palabra):
        if letra in letras_presionadas:
            texto = letra
        else:
            texto = "_"
        mostrar_texto(texto, 50 + i * 40, 150, NEGRO)
    
    mostrar_texto("Letras Usadas: " + " ".join(letras_presionadas),50, 250, ROJO)
    
    dibujar_estructura(pantalla, "imagenes\\2.png", posicion = (50,100), tamaño =(200,150))

    dibujar_cuerpo(errores, lista_animacion_personaje)
    
    if mensaje:
        mostrar_texto(mensaje, 50, 400, ROJO)    
    

# ----------------- VERIFICAR LETRA -----------------
def verificar_letra(letra, palabra, letras_adivinadas):
    # Agregar la letra a letras_adivinadas si no estaba
    # Retornar True si la letra está en la palabra, False si no
    """Captura teclas presionadas y las guarda en una lista si es una letra."""
    if letra.isalpha() and letra not in letras_adivinadas:
            letras_adivinadas.append(letra)
            if letra in palabra:
                return True
    return False
     
    
def mostrar_texto(texto, x, y, color=NEGRO):
    """Dibuja texto en la pantalla en la posición x, y."""
    render = FUENTE.render(texto, True, color)
    pantalla.blit(render, (x, y))   
    

# ----------------- SONIDO -----------------
# pygame.mixer.init()  # Inicializa el motor de sonido
# sonido_error = pygame.mixer.Sound("error.wav")  # Asegurate de tener este archivo

# ----------------- BUCLE PRINCIPAL -----------------

estado_jugar = False

personaje = crear_personaje(x = 200, y= 200)
boton_jugar = boton(x= 150,y= 150, ruta ="assets/boton_empezar.png")


def jugar():
    
    errores = 0

    letras_presionadas = []
    
    lista_palabras = cargar_palabras(archivo)
    
    palabra_random = elegir_palabra(lista_palabras)
     
    mensaje = ""
    tiempo_mensaje = 0
    DURACION_MENSAJE = 1000
 
    ejecutando =  True

    # 1. Cargar palabras desde archivo y elegir una al azar
    # 2. Inicializar estructuras necesarias: letras_adivinadas, errores, reloj, banderas
    # 3. Crear un bucle while que termine al cerrar el juego o al ganar/perder
    # 4. Dentro del bucle:
    #     - Capturar eventos (teclas)
    #     - Verificar letras
    #     - Incrementar errores si corresponde
    #     - Dibujar estado del juego en pantalla
    #     - Verificar condiciones de fin (victoria o derrota)
    #     - Actualizar pantalla
    #     - Controlar FPS

    # Instrucción: este bloque debe ser completado por el estudiante según las consignas
    
    while ejecutando:
        RELOJ.tick(FPS)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False

            if evento.type == pygame.KEYDOWN:
                letra = evento.unicode.upper()
                print(palabra_random)
                if verificar_letra(letra,palabra_random, letras_presionadas):
                    mensaje = "crack"
                else:
                    mensaje = "mal ahi"
                    errores += 1
                tiempo_mensaje = pygame.time.get_ticks()
                
        if mensaje and pygame.time.get_ticks() - tiempo_mensaje > DURACION_MENSAJE:
            mensaje = ""
            
                
                
        if estado_jugar:
            if jugar(archivo, evento, personaje, ANCHO, pantalla, fuente = FUENTE) == False:
                ejecutando == False
        else:
            mostrar_texto(FUENTE, NEGRO, "Ahorcado - ¡Adivina la palabra o seras colgado!", 0, 0, pantalla)
            if dibujo_textos(boton_jugar, pantalla):
                estado_jugar = True      
        
        
        pantalla.fill(BLANCO)
        
        dibujar_juego("imagenes\\fondo_juego.png", palabra_random, letras_presionadas, errores, mensaje )
        
        
        # mostrar_texto("Letras: " + " ".join(letras_presionadas), 50, 50, ROJO)

        palabra_mostrada = [letra if letra in letras_presionadas else "_" for letra in palabra_random]
        if "_" not in palabra_mostrada:
            mostrar_texto("¡Ganaste!", 50, 500, ROJO)
            pygame.display.update()
            pygame.time.wait(2000)
            ejecutando = False

        # Verificar derrota
        if errores >= len(lista_animacion_personaje):
            mostrar_texto("¡Perdiste! Era: " + palabra_random, 50, 500, ROJO)
            pygame.display.update()
            pygame.time.wait(2000)
            ejecutando = False
    
        


        
        
        pygame.display.update()

    pygame.quit()

# No ejecutar el juego automáticamente: solo se invoca desde consola o importación
# Descomentar la línea siguiente para probar el juego terminado:
# jugar()

jugar()