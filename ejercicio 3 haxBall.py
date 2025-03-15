import pygame

pygame.init()
resolution = (720, 580)
ventana = pygame.display.set_mode(resolution)
pygame.display.set_caption("Haxball3")

bola = pygame.image.load("bola.png")
bolarecta = bola.get_rect()
velocidadbola = [0,0]
velo1 = [0,0]
bolarecta.move_ip(0,0)

jugador1 = pygame.image.load("player1.png")
jugador1r = player1.get_rect()

jugador1r.move_ip(0,resolution[1]/2)

jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        jugador1r = jugador1.move(-2,0)
        velo1[0] = -3
    if keys[pygame.K_RIGHT]:
        jugador1r = jugador1.move(2,0)
        velo1[0] = 3
    if keys[pygame.K_UP]:
        jugador1r = jugador1.move(0,-2)
        velo1[1] = -3
    if keys[pygame.K_DOWN]:
        jugador1r = jugador1.move(0,2)
        velo1[1] = 3

    if bolarecta.left < 0 or bolarecta.right > ventana.get_width():
        velocidadbola[0] = -velocidadbola[0]
    if bolarecta.top < 0 or bolarecta.bottom > ventana.get_height():
        velocidadbola[1] = -velocidadbola[1]
    ventana.fill((270, 250, 220))
    ventana.blit(bola, bolarecta)
 
    ventana.blit(jugador1, jugador1r)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()




