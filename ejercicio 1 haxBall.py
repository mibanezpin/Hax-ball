import pygame

pygame.init()

resolution = (720,580)
ventana = pygame.display.set_mode(resolution)
pygame.display.set_caption("Haxball")

jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
 jugando = False
 
    ventana.fill((300, 300, 300))

    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()


