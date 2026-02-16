import random

import pygame.draw

from config import S_W, S_H
from tile import Tile
from utils import load_settings


class Map:
    def __init__(self, new_game=True):
        self.show_map = False
        self.map = None
        self.global_map = []
        self.x, self.y = 4, 4
        if new_game:
            self.create_global_map()
            self.player_pos = 0, 0
        else:
            self.player_pos = self.load_map()
        self.map = self.global_map[self.y][self.x]

    def draw_map(self, screen):
        if self.show_map:
            y_temp = 0
            side = 65
            gap = 5
            depth_y = len(self.global_map)
            depth_x = len(self.global_map[0])
            mini_width = side * depth_x + gap * (depth_x - 1)
            mini_heigh = side * depth_y + gap * (depth_y - 1)
            shift_x = S_W / 3.4 - mini_width / 2
            shift_y = S_H / 2 - mini_heigh / 2
            player_area = [
                (self.x - 1, self.y - 1), (self.x, self.y - 1), (self.x + 1, self.y - 1),
                (self.x - 1, self.y),(self.x,self.y),(self.x + 1, self.y),
                (self.x - 1, self.y + 1), (self.x, self.y + 1), (self.x + 1, self.y + 1)]
            for index,(cell_x,cell_y) in enumerate(player_area):
                if cell_x > depth_x-1:
                    cell_x = 0
                if cell_y > depth_y-1:
                    cell_y = 0
                if cell_x < 0:
                    cell_x = depth_x-1
                if cell_y < 0:
                    cell_y = depth_y-1
                player_area[index] = cell_x,cell_y

            base_player_area = pygame.Rect(mini_width+ shift_x*2,shift_y,S_W-3*shift_x-mini_width,mini_heigh)
            pygame.draw.rect(screen,'black',base_player_area)
            for row_map in self.global_map:
                x_temp = 0
                for map_ in row_map:
                    temp_rect = pygame.Rect(shift_x + (x_temp * (side + gap)), shift_y + (y_temp * (side + gap)), side,
                                            side)
                    if (x_temp,y_temp) in player_area:

                        for cell_x,cell_y in player_area:

                            pygame.draw.rect(screen,'yellow',temp_rect)
                        if x_temp == self.x and y_temp == self.y:
                            pygame.draw.rect(screen, '#ADD8E6', temp_rect)
                        for row in map_:
                            for tile in row:
                                tile.draw_small(screen)

                    else:
                        pygame.draw.rect(screen, 'black', temp_rect)

                    x_temp += 1
                y_temp += 1

    def load_map(self):
        data = load_settings('map.json')
        self.x, self.y = data.get('global_pos')

        for cell_row in data.get('global_map'):
            cell_row_temp = []
            for cell in cell_row:
                local_map = []
                for row in cell:
                    row_temp = []
                    for tile in row:
                        tile_origin = Tile(0, 1, 'fg')
                        tile_origin.load_tile(tile)
                        row_temp.append(tile_origin)
                    local_map.append(row_temp)
                cell_row_temp.append(local_map)
            self.global_map.append(cell_row_temp)
        self.map = self.global_map[self.y][self.x]

        return data.get('player_pos')

    def save_map(self, player_pos):
        data = {'global_pos': (self.x, self.y),
                'player_pos': player_pos,
                'global_map': [],
                }
        for cell_row in self.global_map:
            cell_row_temp = []
            for cell in cell_row:
                local_map = []
                for row in cell:
                    row_temp = []
                    for tile in row:
                        row_temp.append(tile.save_tile())
                    local_map.append(row_temp)
                cell_row_temp.append(local_map)
            data['global_map'].append(cell_row_temp)
        return data

    def change_map(self, side):
        if side == 'right':
            self.x += 1
        elif side == 'left':
            self.x -= 1
        elif side == 'top':
            self.y -= 1
        elif side == 'bottom':
            self.y += 1

        if self.y > len(self.global_map) - 1:
            self.y = 0
        if self.y < 0:
            self.y = len(self.global_map) - 1
        if self.x > len(self.global_map[self.y]) - 1:
            self.x = 0
        if self.x < 0:
            self.x = len(self.global_map[self.y]) - 1

        self.map = self.global_map[self.y][self.x]

    def create_map(self):
        self.map = []
        for y in range(45):
            row = []
            for x in range(80):
                chance = random.randint(0, 100)
                if chance in range(0, 70):
                    tile_type_ = 'sand'
                elif chance in range(71, 90):
                    tile_type_ = 'ground'
                else:
                    tile_type_ = 'rock'
                tile = Tile(x, y, tile_type_)
                row.append(tile)
            self.map.append(row)

    def create_global_map(self):
        for row in range(10):
            one_row = []
            for map_ in range(10):
                self.create_map()
                one_row.append(self.map)
            self.global_map.append(one_row)
