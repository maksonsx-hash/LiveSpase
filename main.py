import pygame
from bUttons import Button
from config import S_W, S_H
from config import switcher

pygame.init()
background_image = pygame.image.load('images/main_background.png')
background_image2 = pygame.image.load('images/background2.png')
background_image = pygame.transform.scale(background_image, (S_W, S_H))
background_image2 = pygame.transform.scale(background_image2, (S_W, S_H))

running = True
screen = pygame.display.set_mode((S_W, S_H))
screen_mod = 'menu'
button_ng = Button(85, 55, 150, 50, '#CCCC99', 'новая игра')
button_cont = Button(85, 135, 150, 50, (128, 128, 0), 'продолжить')
button_save = Button(85, 210, 150, 50, '#00ffff', 'сохранить игру')
button_set = Button(85, S_H - 135, 150, 50, 'green', 'настройки игры')
button_exit = Button(85, S_H - 55, 150, 50, 'green', 'выйти из игры')
set_button_color = Button(85, 55, 150, 50, '#CCCC99', 'фон')
main_buttons_list = [button_ng, button_cont, button_save, button_set, button_exit]
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        screen_mod = 'menu'
    if screen_mod == 'menu':
        print(screen_mod, '3333')
        screen.blit(background_image, (0, 0))

        for button in main_buttons_list:

            button.update(screen)
            if button.pressed:
                if button == button_exit:

                    running = False
                elif button == button_ng:

                    screen_mod = 'newgame'
                    print(screen_mod, '44444')
                elif button == button_cont:

                    screen_mod = 'continue'
                elif button == button_set:
                    screen_mod = 'settings'
                    print(screen_mod, '2222')

                elif button == button_save:
                    screen_mod = 'save'
    elif screen_mod == 'newgame':
        screen.fill((0, 0, 0))
    elif screen_mod == 'continue':
        screen.fill((0, 255, 0))
    elif screen_mod == 'settings':
        screen.fill((255, 0, 0))

        set_button_color.update(screen)

    elif screen_mod == 'save':
        screen.fill((255, 255, 255))

    pygame.display.update()
