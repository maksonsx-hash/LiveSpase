import random

from player import Player
from map import Map
from tile import Tile

import pygame

from init import *
from config import SCREEN_SIZE,  SCREEN_INDEX,BACKGROUND_INDEX

from utils import save_settings


pygame.init()


player = None
map_ = None

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
        screen.blit(background_image_list[BACKGROUND_INDEX], (0, 0))

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


    elif screen_mod == 'game':
        screen.fill((0, 0, 0))
        if player.hit_box.left > S_W:
            map_.change_map('right')
            player.hit_box.left = 0
        elif player.hit_box.right < 0:
            map_.change_map('left')
            player.hit_box.right = S_W
        elif player.hit_box.bottom < 0:
            map_.change_map('top')
            player.hit_box.bottom = S_H
        elif player.hit_box.top > S_H:
            map_.change_map('bottom')
            player.hit_box.top = 0

        for row in map_.map:
            for tile in row:
                tile.draw(screen)
        player.draw(screen)
        player.move()
    elif screen_mod == 'newgame':
        player = Player(S_W/2,S_H/2)
        map_ = Map()
        screen_mod = 'game'
    elif screen_mod == 'continue':

        map_ = Map(new_game=False)
        x,y = map_.player_pos
        player = Player(x,y)
        screen_mod = 'game'
    elif screen_mod == 'settings':
        screen.blit(background_image_list[BACKGROUND_INDEX], (0, 0))
        for button in setting_button_list:
            button.update(screen)

            if button.action_:
                if button == set_button_background:
                    BACKGROUND_INDEX += 1
                    if BACKGROUND_INDEX > len(background_image_list) - 1:
                        BACKGROUND_INDEX = 0
                if button == set_button_size_b:
                    SCREEN_INDEX += 1
                if button == set_button_size_s:
                    SCREEN_INDEX -= 1
                if SCREEN_INDEX > len(SCREEN_SIZE) -1:
                    SCREEN_INDEX = 0
                if SCREEN_INDEX < 0:
                    SCREEN_INDEX = len(SCREEN_SIZE) -1
                text_tuple = SCREEN_SIZE[SCREEN_INDEX]
                screen_size_holder.change_text(text_tuple)

        screen_size_holder.draw(screen)
    elif screen_mod == 'save':
        saved_map = map_.save_map(player_pos=player.hit_box.center)

        save_settings(saved_map, 'map.json')
        print('игра сохранена')
        screen_mod = 'menu'
        if button_cont not in main_buttons_list:
            main_buttons_list.append(button_cont)


    pygame.display.update()
data = {'SCREEN_INDEX':SCREEN_INDEX,'BACKGROUND_INDEX':BACKGROUND_INDEX}
save_settings(data)
print(data)