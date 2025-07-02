import pygame

def crear_ahorcado(x: int, y: int, errores:int = 0, alto:int|float = 0, ancho:int|float = 0, escalado:int|float = 1):
    '''
    Crea al ahorcado permitiendo pasar sus coordenadas donde vaya a
    posicionarse, la posibilidad de cambiar su ancho y largo, al igual
    que su escalado.

    Return dict
    '''
    #carga la imagen del ahorcado. {errores} sera el encargado de pasar de imagen
    imagen = pygame.image.load(f"assets/ahorcado_error0{errores}.png")

    imagen_escalada_alto = int(imagen.get_rect().h * escalado)
    imagen_escalada_ancho = int(imagen.get_rect().w * escalado)

    if (escalado == 1 and alto != 0 and ancho != 0):
        imagen = pygame.transform.scale(imagen, (alto, ancho))
    elif (escalado != 1):
        imagen = pygame.transform.scale(imagen,(
            imagen_escalada_ancho, imagen_escalada_alto))

    return {
        "imagen": imagen.convert_alpha(),
        "x": x,
        "y": y,
        "errores": 0,
        "ancho": imagen.get_rect().w,
        "alto": imagen.get_rect().h,
    }

def dibujar_ahorcado(pantalla: pygame.Surface, ahorcado: dict, errores: int):
    '''
    Dibuja en pantalla al ahorcado, cambiando de imagen si se cometen errores

    No retorna nada
    '''
    pantalla.blit(crear_ahorcado(ahorcado["x"], ahorcado["y"], errores)["imagen"],
                (ahorcado["x"], ahorcado["y"]))