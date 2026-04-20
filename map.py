import random

import pygame.draw

from config import S_W, S_H
from tile import Tile
from krator import Krator
from utils import load_settings
from traps import Trap


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
                [(self.x - 1, self.y - 1), (self.x, self.y - 1), (self.x + 1, self.y - 1)],
                [(self.x - 1, self.y), (self.x, self.y), (self.x + 1, self.y)],
                [(self.x - 1, self.y + 1), (self.x, self.y + 1), (self.x + 1, self.y + 1)]]
            for index_row, row in enumerate(player_area):
                for index, (cell_x, cell_y) in enumerate(row):
                    if cell_x > depth_x - 1:
                        cell_x = 0
                    if cell_y > depth_y - 1:
                        cell_y = 0
                    if cell_x < 0:
                        cell_x = depth_x - 1
                    if cell_y < 0:
                        cell_y = depth_y - 1
                    player_area[index_row][index] = cell_x, cell_y

            base_player_area = pygame.Rect(mini_width + shift_x * 2, shift_y, S_W - 3 * shift_x - mini_width,
                                           mini_heigh)
            pygame.draw.rect(screen, 'black', base_player_area)
            temp_area = []

            for row_map in self.global_map:
                x_temp = 0
                for map_ in row_map:
                    temp_rect = pygame.Rect(shift_x + (x_temp * (side + gap)), shift_y + (y_temp * (side + gap)), side,
                                            side)
                    local_x = 0
                    local_y = 0
                    for index_row, area_row in enumerate(player_area):
                        for index, area in enumerate(area_row):
                            if (x_temp, y_temp) == area:
                                local_x = index
                                local_y = index_row
                            temp_area.append(area)
                    if (x_temp, y_temp) in temp_area:

                        if x_temp == self.x and y_temp == self.y:
                            pygame.draw.rect(screen, '#ADD8E6', temp_rect)
                        else:
                            pygame.draw.rect(screen, 'yellow', temp_rect)
                        tile_size = 2
                        location_gap = 5
                        location_shift_x = mini_width + shift_x * 2 + tile_size * 2
                        location_shift_y = shift_y + location_gap
                        location_depth_y = len(map_['map'])
                        location_depth_x = len(map_['map'][0])

                        tile_width = location_depth_x * tile_size
                        tile_heigh = location_depth_y * tile_size

                        for index_y, row in enumerate(map_['map']):
                            for index_x, tile in enumerate(row):
                                tile_x = location_shift_x + tile_size * index_x + (location_gap + tile_width) * local_x
                                tile_y = location_shift_y + tile_size * index_y + (location_gap + tile_heigh) * local_y
                                tile.draw_small(screen, tile_x, tile_y)




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
                local_map = {'map': [],
                             'krator': None,
                             'trap': None}
                for row in cell.get('map'):
                    row_temp = []
                    for tile in row:
                        tile_origin = Tile(0, 1, 'fg')
                        tile_origin.load_tile(tile)
                        row_temp.append(tile_origin)
                    local_map['map'].append(row_temp)
                krator = cell.get('krator')
                trap = cell.get('trap')

                e_krator = Krator(0,0,'')
                e_krator.load(krator)
                local_map['krator'] = e_krator
                if trap:
                    e_trap = Trap(0,0)
                    e_trap.load(trap)
                    local_map['trap'] = e_trap
                cell_row_temp.append(local_map)
            self.global_map.append(cell_row_temp)
        self.map = self.global_map[self.y][self.x]
        self.time = data['global_timer']

        return data.get('player_pos')

    def save_map(self, timer,current_time ,player_pos):
        data = {'global_pos': (self.x, self.y),
                'player_pos': player_pos,
                'global_map': [],
                'global_timer':(timer,current_time)
                }
        for cell_row in self.global_map:
            cell_row_temp = []
            for cell in cell_row:
                local_map = {'map': [],
                             'krator': None,
                             'trap': None}
                for row in cell.get('map'):
                    row_temp = []
                    for tile in row:
                        row_temp.append(tile.save_tile())
                    local_map['map'].append(row_temp)
                krator = cell.get('krator')
                trap = cell.get('trap')
                local_map['krator'] = krator.save()
                if trap:
                    local_map['trap'] = trap.save()
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

    def create_map(self, type_=None, is_trap = None):
        krator = Krator(random.randint(80,S_W-80),random.randint(80,S_H-80), type_)
        if is_trap:
            trap = Trap(random.randint(80, S_W-80), random.randint(80, S_H-80 ))
        else:
            trap = None
        self.map = {'map': [],
                    'krator': krator,
                    'trap': trap,
                    }
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
            self.map['map'].append(row)

    def create_global_map(self):
        crator_pos = self.random_pos_krator(['gold', 'orange'], 20)
        trap_pos = self.random_pos_krator(['trap'], 20)
        for y in range(1, 11):
            one_row = []
            for x in range(1, 11):
                current_map_pos = x, y
                if current_map_pos in trap_pos['trap']:
                    if current_map_pos in crator_pos ['gold']:
                        self.create_map('gold', 'trap')
                        print(current_map_pos)
                    elif current_map_pos in crator_pos ['orange']:
                        self.create_map('orange', 'trap')
                        print(current_map_pos)
                    else:
                        self.create_map(is_trap='trap')
                else:
                    if current_map_pos in crator_pos ['gold']:
                        self.create_map('gold')
                        print(current_map_pos)
                    elif current_map_pos in crator_pos ['orange']:
                        self.create_map('orange')
                        print(current_map_pos)
                    else:
                        self.create_map()

                one_row.append(self.map)
            self.global_map.append(one_row)

    def random_pos_krator(self,types_krator, max_cell=20):
        bad_pos = {}
        for i in types_krator:
            bad_pos[i] = []
        unic_values = []
        for i in types_krator:
            count = 0
            while count != max_cell // len(types_krator):
                b = random.randint(1, 10), random.randint(1, 10)
                if b in unic_values:
                    continue
                bad_pos[i].append(b)
                unic_values.append(b)
                count += 1
        return bad_pos



