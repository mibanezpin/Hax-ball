import pygame

pygame.init()
ventana = pygame.display.set_mode((720,580))
pygame.display.set_caption("Haxball2")

bola = pygame.image.load("bola.png")
bolarecta = bola.get_rect()

velocidadbola = [0,0]

bolarecta.move_ip(resolution[0]/2, resolution[1]/2)

jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False

    bolarecta = bolarecta.move(speed)

    if bolarecta.left < 0 or bolarecta.right > ventana.get_width():
        velocidadbola[0] = -velocidadbola[0]
            
    if bolarecta.top < 0 or bolarecta.bottom > ventana.get_height():
        velocidadbola[1] = -velocidadbola[1]
    
    ventana.fill((270, 250, 220))

    ventana.blit(bola, bolarecta)
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()



