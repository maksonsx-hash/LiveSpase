import pygame
from bUttons import Button
from config import S_W, S_H


pygame.init()

running = True
screen = pygame.display.set_mode((S_W, S_H))
button_ng = Button(50, 45, 50, 20,'blue')
button_cont = Button(S_W/2-200, S_H/2-200, 100,50,'green')
button_save = Button(S_W/2-200, S_H/2-200, 100,50,'green')
button_set = Button(S_W/2-200, S_H/2-200, 100,50,'green')
button_exit = Button(S_W/2-200, S_H/2-200, 100,50,'green')
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    button_ng.update(screen )
    button_cont.update(screen)
    pygame.display.update()
