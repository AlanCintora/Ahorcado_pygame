import pygame

def textos(x, y, imagen, escalado = 1):
    '''
    
    
    
    '''
    ancho = imagen.get_width()
    alto = imagen.get_height()
    imagen = pygame.transform.scale(imagen, (int(ancho * escalado), int(alto * escalado)))
    rectangulo_imagen = imagen.get_rect()
    rectangulo_imagen.topleft = (x, y)

    return {
        "imagen": imagen,
        "rect": rectangulo_imagen,
        "clickeado": False
    }

def dibujo_textos(texto: function, pantalla):
    '''
    
    
    
    '''
    accion = False

    mouse = pygame.mouse.get_pos()

    if texto.rect.collidepoint(mouse):
        if pygame.mouse.get_pressed()[0] == 1 and texto["clickeado"] == False:
            accion = True
            texto["clickeado"] = True
    if pygame.mouse.get_pressed()[0] == 0:
        texto["clickeado"] = False
    
    pantalla.blit(texto, (texto["rect".x], texto["rect"].y))

    return accion