import pygame
import random


class Traps:
    def __init__(self):

        self.w = random.randint(80, 160)

        self.chose_color(type_)
        self.color = (self.a, self.b, self.c)
        self.hit_box = pygame.Rect(x, y, self.w, self.w)
        self.hit_box.center = (x, y)