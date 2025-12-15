import pygame
from text_holder import TextHolder

from bUttons import Button
from config import S_W, S_H

button_ng = Button(85, 55, 150, 50, '#CCCC99', 'новая игра')
button_cont = Button(85, 135, 150, 50, (128, 128, 0), 'продолжить')
button_save = Button(85, 210, 150, 50, '#00ffff', 'сохранить игру')
button_set = Button(85, S_H - 135, 150, 50, 'green', 'настройки игры')
button_exit = Button(85, S_H - 55, 150, 50, 'green', 'выйти из игры')

set_button_background = Button(85, 55, 150, 50, '#CCCC99', 'фон')
set_button_size_b = Button(500, 55, 75, 50, 'green', '>')
set_button_size_s = Button(200, 55, 75, 50, 'green', '<')
screen_size_holder = TextHolder(300, 55, 75, 50, 'white', f'{S_W}-{S_H}')

main_buttons_list = [button_ng, button_cont, button_save, button_set, button_exit]
setting_button_list = [set_button_background, set_button_size_b, set_button_size_s]

background_image = pygame.image.load('images/main_background1.png')
background_image2 = pygame.image.load('images/main_background2.png')
background_image = pygame.transform.scale(background_image, (S_W, S_H))
background_image2 = pygame.transform.scale(background_image2, (S_W, S_H))
background_image_list = [background_image, background_image2]
background_index = 0