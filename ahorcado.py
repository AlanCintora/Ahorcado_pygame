import pygame

def crear_ahorcado(x, y, fallo: int, alto = 0, ancho = 0, escalado = 1):
    '''
    
    
    
    '''
    imagen = pygame.image.load(f"assets/ahorcado_error0{fallo}.png")

    imagen_escalada_alto = int(imagen.get_rect().h * escalado)
    imagen_escalada_ancho = int(imagen.get_rect().w * escalado)

    if (escalado == 1 and alto != 0 and ancho != 0):
        imagen = pygame.transform.scale(imagen, (alto, ancho)).convert_alpha()
    elif (escalado != 1):
        imagen = pygame.transform.scale(imagen,(
            imagen_escalada_ancho, imagen_escalada_alto)).convert_alpha()
    else:
        imagen = imagen.convert_alpha()

    return {
        "imagen": imagen,
        "x": x,
        "y": y,
        "ancho": imagen.get_rect().w,
        "alto": imagen.get_rect().h,
    }

def dibujar_ahorcado(pantalla, ahorcado):
    '''
    
    
    
    '''
    pantalla.blit(ahorcado["imagen"], (ahorcado["x"], ahorcado["y"]))