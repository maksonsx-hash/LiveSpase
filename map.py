import random
from tile import Tile
from utils import load_settings


class Map:
    def __init__(self, new_game=True):
        self.map = None
        self.global_map = []
        self.x, self.y = 4, 4
        if new_game:
            self.create_global_map()
            self.player_pos = 0,0
        else:
            self.player_pos = self.load_map()
        self.map = self.global_map[self.y][self.x]

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


    def save_map(self,player_pos):
        data = {'global_pos':(self.x,self.y),
                'player_pos':player_pos,
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
        for row in range (10):
            one_row = []
            for map_ in range(10):
                self.create_map()
                one_row.append(self.map)
            self.global_map.append(one_row)