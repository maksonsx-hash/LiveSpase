import pygame
from bUttons import Button
from config import S_W, S_H

pygame.init()

running = True
screen = pygame.display.set_mode((S_W, S_H))
button_ng = Button(85, 55, 150, 50, 'blue', 'новая игра')
button_cont = Button(85, 135, 150, 50, 'green', 'продолжить')
button_save = Button(85, 210, 150, 50, 'green', 'сохранить игру')
button_set = Button(85, S_H-135, 150, 50, 'green', 'настройки игры')
button_exit = Button(85, S_H-55, 150, 50, 'green', 'выйти из игры')
main_buttons_list = [button_ng, button_cont, button_save, button_set, button_exit]
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for button in main_buttons_list:
        button.update(screen)

    pygame.display.update()
