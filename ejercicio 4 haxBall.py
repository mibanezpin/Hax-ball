    if bolarecta.colliderect(jugador1r):
        velocidadbola[0]=-(float(velocidadbola[0])*0.95)
        velocidadbola[1]=-(float(velocidadbola[1])*0.95)

        if keys[pygame.K_SPACE]:
            velocidadbola[0] = velo1[0]
            velocidadbola[1] = velo1[1]
    bolarecta = bolarecta.move(velocidadbola)

    timer += pygame.time.get_ticks()

    if timer >7500:
timer = 0
        if velocidadbola[0] > 0:
            velocidadbola[0] = velocidadbola[0]-0.01
        elif velocidadbola[0] < 0:
            velocidadbola[0] = velocidadbola[0]+0.01
        if velocidadbola[1] > 0:
            velocidadbola[1] = velocidadbola[1]-0.01
        elif velocidadbola[1] < 0:
            velocidadbola[1] = velocidadbola[1]+0.01

        for gameObj in gameObjects:
            if gameObj.type == "bola":
                if (gameObj.x - self.x)**2 + (gameObj.y - self.y)**2 <= (gameObj.radius + self.radius)**2:
                   if keys[pygame.K_SPACE]:
                       gameObj.dy = self.dy
                       gameObj.dx = self.dx
timer = pygame.time.get_ticks()

if timer > 7500:
    timer = 0
    if self.dx > 0:
        self.dx -= 0.01
    elif self.dx < 0:
        self.dx += 0.01
    if self.dy > 0:
        self.dy -= 0.01
    elif self.dy < 0:
        self.dy += 0.01
class game():

    def __init__(self):
        pygame.init()
        
        self.screen = pygame.display.set_mode(resolution)
 self.clock = pygame.time.Clock()
        self.gameObjects = []
        self.gameObjects.append(Bola())
        self.gameObjects.append(Jugador())

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

    def run(self):

        while True:
            self.handleEvents()

            for gameObj in self.gameObjects:
                gameObj.update(self.gameObjects)

            self.screen.fill(white)

            for gameObj in self.gameObjects:
                gameObj.draw(self.screen)

            self.clock.tick(60)
            pygame.display.flip()

game().run()




