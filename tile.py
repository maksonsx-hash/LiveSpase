import pygame
import random


class Tile:
    def __init__(self, x, y, type_):
        size = 16
        self.hit_box = pygame.Rect(x * size, y * size, size, size)
        self.type_ = type_
        self.color = None
        self.change_color()


    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.hit_box)

    def change_color(self):
        if self.type_ == 'sand':
            self.color = random.choice([(203, 189, 147), (190, 194, 147), (210, 190, 147)])
        elif self.type_ == 'rock':
            self.color = random.choice([(173, 165, 135), (180, 165, 135), (160, 170, 135)])
        elif self.type_ == 'ground':
            self.color = random.choice([(162, 101, 62), (170, 106, 62), (150, 101, 67)])
        else:
            self.color = (134, 0, 255)
