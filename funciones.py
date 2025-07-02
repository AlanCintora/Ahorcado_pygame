import random
import pygame
import sys
from personaje import *
from ahorcado import *
from colores import *

pygame.mixer.init()
sonido_error = pygame.mixer.Sound("assets/error.wav")
sonido_win = pygame.mixer.Sound("assets/bravo.wav")
sonido_loss = pygame.mixer.Sound("assets/muerte.wav")

sonido_error.set_volume(0.1)
sonido_win.set_volume(0.1)
sonido_loss.set_volume(0.1)

# ----------------- CARGAR PALABRASS -----------------
def cargar_palabras(nombre_archivo: str) -> list:
    '''
    Lee las palabras desde un archivo de texto y devuelve una lista
    
    Return list
    '''
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
def elegir_palabra(lista_palabras: list) -> str | None:
    '''
    Elige una palabra al azar que se encuentre dentro de la lista
    y convierte las teclas en mayusculas
    
    Return str | None
    '''
    if lista_palabras:
        return random.choice(lista_palabras).upper()
    else:
        return None
# ----------------- VERIFICAR LETRA PRESIONADA -----------------
def verificar_letra(letra: pygame.key, palabra: str, letras_adivinadas: list) -> bool:
    '''
    Captura teclas presionadas, las guarda en una lista, se verifica si
    la letra se encuentra dentro de la palabra
    
    Return bool
    '''
    letras_adivinadas.append(letra)
    
    return letra in palabra

# ----------------- DIBUJO DE CRUCES -----------------
def dibujar_cruces(errores: int, pantalla: pygame.Surface, color) -> None:
    '''
    Dibuja lineas que forman una cruz dependiendo de los errores que se
    vayan cometiendo
    
    No return
    '''
    for i in range(errores):
        # Cada cruz se desplaza 50 píxeles hacia la derecha
        x = 30 + i * 60
        y = 30
        pygame.draw.line(pantalla, color, (x, y), (x + 30, y + 30), 5)
        pygame.draw.line(pantalla, color, (x + 30, y), (x, y + 30), 5)

# ----------------- CREACION Y CARGA DE BOTON -----------------
def boton(x: int, y: int, ruta: str, escalado: int|float = 1) -> dict:
    '''
    Carga un boton permitiendo pasar sus coordenadas donde vaya a
    posicionarse, el path de la imagen y la posibilidad de cambiar
    su escalado
    
    Return dict
    '''
    image = pygame.image.load(ruta)
    image_escalada = pygame.transform.scale(image, (int(image.get_width() * escalado), int(image.get_height() * escalado)))
    rectangulo = image_escalada.get_rect()
    rectangulo.topleft = (x, y)

    return {
        "imagen": image_escalada.convert_alpha(),
        "rect": rectangulo,
        "clickeado": False
    }

def dibujo_boton(boton: dict, pantalla : pygame.Surface) -> bool:
    '''
    Dibuja el boton en la pantalla y verifica si fue apretado
    
    Return bool
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

def mostrar_texto(fuente: pygame.font, color: tuple, texto: str, x: int, y: int, pantalla: pygame.surface) -> None:
    '''
    Dibuja el texto en pantalla
    
    No return
    '''
    superficie = fuente.render(texto, True, color)
    pantalla.blit(superficie, (x, y))

def main_texto(fuente_titulo: pygame.font, fuente_normal: pygame.font, pantalla: pygame.surface) -> None:
    '''
    Dibuja en pantalla los textos del menu del juego
    
    No return
    '''
    mostrar_texto(fuente_titulo, NEGRO, "Ahorcado - ¡Adivina la palabra!", 150, 50, pantalla)
    mostrar_texto(fuente_normal, NEGRO, "Aprieta la letra que creas que forma parte de la palabra.", 70, 145, pantalla)
    mostrar_texto(fuente_normal, NEGRO, "Solo tenes 6 intentos asi que usalos sabiamente o...", 90, 175, pantalla)
    mostrar_texto(fuente_titulo, NEGRO, "SERAS COLGADO", 240, 240, pantalla)

def dibujar_juego(fuente: pygame.font, palabra: str, letras_presionadas: list, pantalla: pygame.surface, mensaje: str):
    '''
    Dibuja los guiones de la palabra oculta, las teclas presionadas,
    cambia los guiones por las letras que se encuentran en la palabra y
    un mensaje de si se apreto la letra: bien, mal, ya fue presionada
    
    No return
    '''
    for i, letra in enumerate(palabra):
        if letra in letras_presionadas:
            texto = letra
        else:
            texto = "_"
        mostrar_texto(fuente, NEGRO, texto, 400 + i * 40, 150, pantalla)
    
    mostrar_texto(fuente, ROJO, "Letras Usadas: " + " ".join(letras_presionadas), 10, 350, pantalla)
    
    if mensaje:
        mostrar_texto(fuente, ROJO, mensaje, 185, 400, pantalla)

def resultado_juego(errores: int, palabra_mostrada: list, palabra_random: str, fuente: pygame.font, pantalla: pygame.surface):
    '''
    Dibuja un texto dependiendo de si se ganó o perdió, emitiendo un sonido
    en cada caso
    
    No return
    '''
    if "_" not in palabra_mostrada:
        sonido_win.play()
        mostrar_texto(fuente, NEGRO, "¡Ganaste!", 400, 180, pantalla)
        pygame.display.update()
        pygame.time.wait(2000)
        pygame.quit()
        sys.exit()
    
    if errores == 6:
        sonido_loss.play()
        mostrar_texto(fuente, NEGRO, "¡Perdiste! Era: " + palabra_random, 400, 180, pantalla)
        pygame.display.update()
        pygame.time.wait(2000)
        pygame.quit()
        sys.exit()


def jugar(evento: pygame.event, letra: pygame.key, palabra_random: str, letras_presionadas: list,
        tiempo_actual: pygame.time, duracion_mensaje: int, tiempo_mensaje: int,
        personaje: dict, ahorcado: dict, ancho_pantalla: int, pantalla: pygame.surface,
        fuente: pygame.font, mensaje: str) -> None:
    '''
    Encargado del funcionamiento principal del juego y dibujo del mismo
    en pantalla
     
    No return
    '''
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
                sonido_error.play()

    if tiempo_actual - tiempo_mensaje > duracion_mensaje:
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