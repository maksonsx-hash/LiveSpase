import pygame
import random


class Tile:
    def __init__(self, x, y):
        size = 16
        self.hit_box = pygame.Rect(x * size, y * size, size, size)
        self.color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.hit_box)
