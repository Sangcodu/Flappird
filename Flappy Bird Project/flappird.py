import pygame, sys
pygame.init()
screen = pygame.display.set_mode((423, 600))
Clock = pygame.time.clock()
bg = pygame.image.load('assets/background-night.png')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            sys.exit()
    pygame.display.update()
    Clock.tick(120)