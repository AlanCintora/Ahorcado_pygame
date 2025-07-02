import random
import pygame
import sys
from personaje import *
from ahorcado import *
from colores import *

### facu
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

def verificar_letra(letra, palabra, letras_adivinadas):
    # Agregar la letra a letras_adivinadas si no estaba
    # Retornar True si la letra está en la palabra, False si no
    """Captura teclas presionadas y las guarda en una lista si es una letra."""
    if letra.isalpha() and letra not in letras_adivinadas:
            letras_adivinadas.append(letra)
            if letra in palabra:
                return True
    return False

### alan
def dibujar_cruces(errores, pantalla, ROJO):
    for i in range(errores):
        # Cada cruz se desplaza 50 píxeles hacia la derecha
        x = 50 + i * 60
        y = 50
        pygame.draw.line(pantalla, ROJO, (x, y), (x + 30, y + 30), 5)
        pygame.draw.line(pantalla, ROJO, (x + 30, y), (x, y + 30), 5)

### matias
def boton(x, y, ruta, escalado = 1):
    '''
    
    
    
    '''
    image = pygame.image.load(ruta)
    ancho = image.get_width()
    alto = image.get_height()
    image_escalada = pygame.transform.scale(image, (int(ancho * escalado), int(alto * escalado)))
    rectangulo = image_escalada.get_rect()
    rectangulo.topleft = (x, y)

    return {
        "imagen": image_escalada.convert_alpha(),
        "rect": rectangulo,
        "clickeado": False
    }

def dibujo_boton(boton, pantalla):
    '''
    
    
    
    '''
    accion = False
    mouse = pygame.mouse.get_pos()

    if boton["rect"].collidepoint(mouse):
        if pygame.mouse.get_pressed()[0] == 1 and boton["clickeado"] == False:
            accion = True
            boton["clickeado"] = True
    if pygame.mouse.get_pressed()[0] == 0:
        boton["clickeado"] = False
    
    pantalla.blit(boton["imagen"], boton["rect"])

    return accion

def mostrar_texto(fuente, color, texto, x, y, pantalla):
    superficie = fuente.render(texto, True, color)
    pantalla.blit(superficie, (x, y))

# def definir_resultado(errores, palabra_random, palabra_mostrada, color):
#     '''
    
    
    
#     '''
#     if "_" not in palabra_mostrada:
#         mostrar_texto("¡Ganaste!", 50, 500, color)
        
#     # Verificar derrota
#     if errores >= 7:
#         mostrar_texto("¡Perdiste! Era: " + palabra_random, 50, 500, color)

#     pygame.display.update()
#     pygame.time.wait(2000)

#     return False

def dibujar_juego(fuente, palabra, letras_presionadas, pantalla, mensaje=""):
    # Llenar fondo, mostrar palabra oculta, letras ingresadas
    
    for i, letra in enumerate(palabra):
        if letra in letras_presionadas:
            texto = letra
        else:
            texto = "_"
        mostrar_texto(fuente, NEGRO, texto, 50 + i * 40, 150, pantalla)
    
    mostrar_texto(fuente, ROJO, "Letras Usadas: " + " ".join(letras_presionadas), 50, 250, pantalla)
    
    ## dibujar_estructura(pantalla, "imagenes\\2.png", posicion = (50,100), tamaño =(200,150))

    if mensaje:
        mostrar_texto(fuente, ROJO, mensaje, 50, 400, pantalla)

def jugar(evento, letra , palabra_random, letras_presionadas, duracion_msj, personaje, ahorcado, ancho_pantalla, pantalla, fuente, mensaje):
    '''
     
     
     
    '''
    tiempo_acual = pygame.time.get_ticks()
    tiempo_mensaje = 0

    if letra != "" and verificar_letra(letra, palabra_random, letras_presionadas):
        mensaje = "CRACK!"
    elif letra != "" and verificar_letra(letra, palabra_random, letras_presionadas) == False:
        mensaje = "MAL AHI!"
        ahorcado["errores"] += 1
        print(ahorcado["errores"])

    if evento.type == pygame.KEYDOWN:
        if evento.key == pygame.K_ESCAPE:
            pygame.quit()
                
    if mensaje and tiempo_acual - tiempo_mensaje > duracion_msj:
        mensaje = ""
        tiempo_mensaje = tiempo_acual
        
    # Movimiento con teclado
    movimiento(personaje, pygame.key.get_pressed(), ancho_pantalla)

    # Dibujar todo
    dibujar_personaje(pantalla, personaje)
    dibujar_ahorcado(
        pantalla, ahorcado, ahorcado["errores"])
    dibujar_cruces(ahorcado["errores"], pantalla, ROJO)
    dibujar_juego(fuente, palabra_random, letras_presionadas, pantalla)

    palabra_mostrada = [letra if letra in letras_presionadas else "_" for letra in palabra_random]
    if "_" not in palabra_mostrada:
        mostrar_texto(fuente, NEGRO, "¡Ganaste!", 50, 500, pantalla)
        pygame.display.update()
        pygame.time.wait(2000)
        pygame.quit()
    # Verificar derrota
    if ahorcado["errores"] == 6:
        mostrar_texto(fuente, NEGRO, "¡Perdiste! Era: " + palabra_random, 50, 500, pantalla)
        pygame.display.update()
        pygame.time.wait(2000)
        pygame.quit()





# def procesar_tecla(letra, palabra, letras_adivinadas, errores, sonido_error):
#     """
#     Procesa una letra ingresada por el jugador.
#     - letra: la tecla presionada
#     - palabra_secreta: palabra que debe adivinarse
#     - letras_adivinadas: lista de letras ya ingresadas
#     - errores: cantidad de errores hasta ahora
#     - sonido_error: sonido a reproducir si se equivoca
#     Devuelve: (acierto: bool, errores: int)
#     """
#     letra = letra.upper()
#     if letra.isalpha() and letra not in letras_adivinadas:
#         letras_adivinadas.append(letra)
#         if letra in palabra_secreta:
#             return True, errores
#         else:
#             sonido_error.play()
#             errores += 1
#     return False, errores

