import pygame
import random


class Player:
    def __init__(self, x, y):

        self.hit_box = pygame.Rect(x, y, 16, 24)
        self.speed = 5
        self.color = (0, 0, 0)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.hit_box)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.hit_box.y -= self.speed
        if keys[pygame.K_s]:
            self.hit_box.y += self.speed
        if keys[pygame.K_a]:
            self.hit_box.x -= self.speed
        if keys[pygame.K_d]:
            self.hit_box.x += self.speed
