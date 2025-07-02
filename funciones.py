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
    letras_adivinadas.append(letra)
    
    return letra in palabra

### alan
def dibujar_cruces(errores, pantalla, color):
    for i in range(errores):
        # Cada cruz se desplaza 50 píxeles hacia la derecha
        x = 30 + i * 60
        y = 30
        pygame.draw.line(pantalla, color, (x, y), (x + 30, y + 30), 5)
        pygame.draw.line(pantalla, color, (x + 30, y), (x, y + 30), 5)

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

def main_texto(fuente_titulo, fuente_normal, pantalla):
    mostrar_texto(fuente_titulo, NEGRO, "Ahorcado - ¡Adivina la palabra!", 150, 50, pantalla)
    mostrar_texto(fuente_normal, NEGRO, "Aprieta la letra que creas que forma parte de la palabra.", 70, 145, pantalla)
    mostrar_texto(fuente_normal, NEGRO, "Solo tenes 6 intentos asi que usalos sabiamente o...", 90, 175, pantalla)
    mostrar_texto(fuente_titulo, NEGRO, "SERAS COLGADO", 240, 240, pantalla)

def dibujar_juego(fuente, palabra, letras_presionadas, pantalla, mensaje):
    # Llenar fondo, mostrar palabra oculta, letras ingresadas
    
    for i, letra in enumerate(palabra):
        if letra in letras_presionadas:
            texto = letra
        else:
            texto = "_"
        mostrar_texto(fuente, NEGRO, texto, 400 + i * 40, 150, pantalla)
    
    mostrar_texto(fuente, ROJO, "Letras Usadas: " + " ".join(letras_presionadas), 10, 350, pantalla)
    
    mostrar_texto(fuente, ROJO, mensaje, 200, 400, pantalla)

def resultado_juego(errores, palabra_mostrada, palabra_random, fuente, pantalla):
    '''
    
    
    
    '''
    if "_" not in palabra_mostrada:
        mostrar_texto(fuente, NEGRO, "¡Ganaste!", 400, 180, pantalla)
        pygame.display.update()
        pygame.time.wait(2000)
        pygame.quit()
        sys.exit()
    
    if errores == 6:
        mostrar_texto(fuente, NEGRO, "¡Perdiste! Era: " + palabra_random, 400, 180, pantalla)
        pygame.display.update()
        pygame.time.wait(2000)
        pygame.quit()
        sys.exit()

def jugar(evento, letra , palabra_random, letras_presionadas, tiempo_mensaje, personaje, ahorcado, ancho_pantalla, pantalla, fuente, mensaje):
    '''
     
     
     
    '''
    tiempo_actual = pygame.time.get_ticks()
    if evento.type == pygame.KEYDOWN:
        if evento.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()

    if letra != "":
        if letra in letras_presionadas:
            mensaje = "LETRA YA PRESIONADA!"
        else:
            if verificar_letra(letra, palabra_random, letras_presionadas):
                mensaje = "BIEN!"
            else:
                mensaje = "MAL!"
                ahorcado["errores"] += 1
                print(ahorcado["errores"])

    if tiempo_actual == tiempo_mensaje:
        mensaje = ""

    # Movimiento con teclado
    movimiento(personaje, pygame.key.get_pressed(), ancho_pantalla)

    # Dibujar todo
    dibujar_juego(fuente, palabra_random, letras_presionadas, pantalla, mensaje)
    dibujar_personaje(pantalla, personaje)
    dibujar_ahorcado(
        pantalla, ahorcado, ahorcado["errores"])
    dibujar_cruces(ahorcado["errores"], pantalla, ROJO)

    # Verificar derrota
    palabra_mostrada = [letra if letra in letras_presionadas else "_" for letra in palabra_random]

    resultado_juego(ahorcado["errores"], palabra_mostrada, palabra_random, fuente, pantalla)
    

