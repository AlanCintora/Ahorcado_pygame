import pygame
    

def movimiento(personaje, tecla, ancho_pantalla, velocidad = 10):
    '''
    
    
    
    '''
    if tecla[pygame.K_RIGHT]:
        personaje["x"] += velocidad
        if personaje["x"] >= ancho_pantalla - personaje["ancho"]:
            personaje["x"] = ancho_pantalla - personaje["ancho"]
        personaje["imagen"] = crear_personaje(0, 0, accion= "walk")["imagen"]
    if tecla[pygame.K_LEFT]:
        personaje["x"] -= velocidad
        if personaje["x"] <= 0:
            personaje["x"] = 0
        personaje["imagen"] = crear_personaje(0, 0, accion= "walk", vuelta= True)["imagen"]
    if not tecla[pygame.K_LEFT] and not tecla[pygame.K_RIGHT]:
        personaje["imagen"] = crear_personaje(0, 0, accion= "stay")["imagen"]
    if tecla[pygame.K_LEFT] and tecla[pygame.K_RIGHT]:
        personaje["imagen"] = crear_personaje(0, 0, accion= "stay")["imagen"]

def crear_personaje(x, y, accion = "stay", alto = 0, ancho = 0, escalado = 1, vuelta = False):
    '''
    
    
    
    '''
    if accion == "stay":
        imagen = pygame.image.load("assets/cuphead_stay.png")
    elif accion == "walk":
        imagen = pygame.image.load("assets/cuphead_walk.png")

    imagen_escalada_alto = int(imagen.get_rect().h * escalado)
    imagen_escalada_ancho = int(imagen.get_rect().w * escalado)

    if (escalado == 1 and alto != 0 and ancho != 0):
        imagen = pygame.transform.scale(
            imagen, (alto, ancho))
    elif (escalado != 1):
        imagen = pygame.transform.scale(
            imagen,(imagen_escalada_ancho, imagen_escalada_alto))

    if (vuelta):
        imagen = pygame.transform.flip(imagen, True, False)

    return {
        "imagen": imagen.convert_alpha(),
        "x": x,
        "y": y,
        "ancho": imagen.get_rect().w,
        "alto": imagen.get_rect().h,
    }

def dibujar_personaje(pantalla, personaje):
    '''
    
    
    
    '''
    pantalla.blit(personaje["imagen"], (personaje["x"], personaje["y"]))