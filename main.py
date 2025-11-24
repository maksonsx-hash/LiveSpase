import pygame
from bUttons import Button
from config import S_W, S_H


pygame.init()

running = True
screen = pygame.display.set_mode((S_W, S_H))
botton = Button(S_W/2, S_H/2, 30, 30)
botton_2 = Button(S_W/2-200, S_H/2-200, 100,50)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    botton.draw(screen, )
    botton_2.draw(screen)
    pygame.display.update()
