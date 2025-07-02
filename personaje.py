import pygame

pygame.mixer.init()
# SONIDO ERROR
sonido_collision = pygame.mixer.Sound("assets/collition_cuphead.wav")
sonido_collision.set_volume(0.1)
def crear_personaje(x: int, y: int, accion: str = "stay", alto: int = 0, ancho: int = 0, escalado: int|float = 1, vuelta: bool = False) -> dict:
    '''
    Crea al personaje permitiendo pasar sus coordenadas donde vaya a
    posicionarse, el estado del personaje si esta quieto o caminando,
    la posibilidad de cambiar su alto y ancho, al igual que su escalado, y,
    por ultimo, si se giró.
    
    Return dict
    '''
    if accion == "stay":
        imagen = pygame.image.load("assets/cuphead_stay.png")
    elif accion == "walk":
        imagen = pygame.image.load("assets/cuphead_walk.png")

    rect = imagen.get_rect()
    imagen_escalada_alto = int(rect.h * escalado)
    imagen_escalada_ancho = int(rect.w * escalado)

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
        "ancho": rect.w,
        "alto": rect.h,
    }

def movimiento(personaje: dict, tecla: pygame.key, ancho_pantalla: int|float, velocidad: int|float = 10) -> None:
    '''
    Mueve al personaje dependiendo de las teclas presionadas (flechas derecha e izquierda),
    pudiendo establecer su velocidad.
    
    No return
    '''
    if tecla[pygame.K_RIGHT]:
        personaje["x"] += velocidad
        if personaje["x"] >= ancho_pantalla - personaje["ancho"] - 15:
            personaje["x"] = ancho_pantalla - personaje["ancho"] - 15
            sonido_collision.play()
        personaje["imagen"] = crear_personaje(0, 0, accion= "walk")["imagen"]
    if tecla[pygame.K_LEFT]:
        personaje["x"] -= velocidad
        if personaje["x"] <= 0:
            personaje["x"] = 0
            sonido_collision.play()
        personaje["imagen"] = crear_personaje(0, 0, accion= "walk", vuelta= True)["imagen"]
    if not tecla[pygame.K_LEFT] and not tecla[pygame.K_RIGHT]:
        personaje["imagen"] = crear_personaje(0, 0, accion= "stay")["imagen"]
    if tecla[pygame.K_LEFT] and tecla[pygame.K_RIGHT]:
        personaje["imagen"] = crear_personaje(0, 0, accion= "stay")["imagen"]

def dibujar_personaje(pantalla: pygame.Surface, personaje: dict) -> None:
    '''
    Dibuja en pantalla al personaje
    
    No return
    '''
    pantalla.blit(personaje["imagen"], (personaje["x"], personaje["y"]))