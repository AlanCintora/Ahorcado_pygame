import pygame

def texto(x, y, ruta, escalado = 1):
    '''
    
    
    
    '''
    image = pygame.image.load(ruta)
    ancho = image.get_width()
    alto = image.get_height()
    image_escalada = pygame.transform.scale(image, (int(ancho * escalado), int(alto * escalado)))
    rectangulo = image_escalada.get_rect()
    rectangulo.topleft = (x, y)
    clickeado = False

    return {
        "imagen": image_escalada.convert_alpha(),
        "rect": rectangulo,
        "clickeado": clickeado
    }

def dibujo_textos(texto, pantalla):
    '''
    
    
    
    '''
    accion = False
    mouse = pygame.mouse.get_pos()

    if texto["rect"].collidepoint(mouse):
        if pygame.mouse.get_pressed()[0] == 1 and texto["clickeado"] == False:
            accion = True
            texto["clickeado"] = True
    if pygame.mouse.get_pressed()[0] == 0:
        texto["clickeado"] = False
    
    pantalla.blit(texto["imagen"], (texto["rect"].x, texto["rect"].y))

    return accion