import pygame

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

def dibujo_textos(boton, pantalla):
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