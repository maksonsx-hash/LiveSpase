
from init import *



pygame.init()


running = True
screen = pygame.display.set_mode((S_W, S_H))
clock = pygame.time.Clock()
screen_mod = 'menu'


while running:
    clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        screen_mod = 'menu'
    if screen_mod == 'menu':
        screen.blit(background_image_list[background_index], (0, 0))

        for button in main_buttons_list:
            button.update(screen)

            if button.action_:
                if button == button_exit:
                    running = False
                elif button == button_ng:
                    screen_mod = 'newgame'
                elif button == button_cont:
                    screen_mod = 'continue'
                elif button == button_set:
                    screen_mod = 'settings'
                elif button == button_save:
                    screen_mod = 'save'
    elif screen_mod == 'newgame':
        screen.fill((0, 0, 0))
    elif screen_mod == 'continue':
        screen.fill((0, 255, 0))
    elif screen_mod == 'settings':
        screen.blit(background_image_list[background_index], (0, 0))
        for button in setting_button_list:
            button.update(screen)

            if button.action_:
                if button == set_button_background:
                    background_index += 1
                    if background_index > len(background_image_list) - 1:
                        background_index = 0
        screen_size_holder.draw(screen)
    elif screen_mod == 'save':
        screen.fill((255, 255, 255))

    pygame.display.update()
