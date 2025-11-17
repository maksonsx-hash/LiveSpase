import pygame


pygame.init()

S_W = 800
S_H = 800

running = True
screen = pygame.display.set_mode((S_W, S_H))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()




