import pygame
import random


class Tile:
    def __init__(self, x, y, type_):
        size = 16
        small_size = 2
        self.hit_box = pygame.Rect(x * size, y * size, size, size)
        self.small_hit_box = pygame.Rect(x * small_size, y * small_size, small_size, small_size)
        self.type_ = type_
        self.color = None
        self.change_color()

    def save_tile(self):
        data = {'size': self.hit_box.height,
                'pos': (self.hit_box.x, self.hit_box.y),
                'small_pos':(self.small_hit_box.x, self.small_hit_box.y),
                'type': self.type_,
                'color': self.color, }
        return data

    def load_tile(self, data):
        self.hit_box = pygame.Rect(data.get('pos')[0],
                                   data.get('pos')[1],
                                   data.get('size'),
                                   data.get('size'))
        self.small_hit_box = pygame.Rect(data.get('small_pos')[0],
                                         data.get('small_pos')[1],
                                         2,
                                         2)
        self.type_ = data.get('type')
        self.color = data.get('color')

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.hit_box)

    def draw_small(self, surface):
        pygame.draw.rect(surface, self.color, self.small_hit_box)

    def change_color(self):
        if self.type_ == 'sand':
            self.color = random.choice([(203, 189, 147), (190, 194, 147), (210, 190, 147)])
        elif self.type_ == 'rock':
            self.color = random.choice([(173, 165, 135), (180, 165, 135), (160, 170, 135)])
        elif self.type_ == 'ground':
            self.color = random.choice([(162, 101, 62), (170, 106, 62), (150, 101, 67)])
        else:
            self.color = (134, 0, 255)
