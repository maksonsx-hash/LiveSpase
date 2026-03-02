import random

import pygame

S_W = 500
S_H = 500
screen = pygame.display.set_mode((S_W, S_H))


class Krator:
    def __init__(self, x, y):
        self.w = random.randint(80, 160)
        self.h = int(self.w/2)
        x2 = int(self.h / 2)
        y2 = int(self.h / 2)
        self.hit_box = pygame.Rect(x, y, self.w, self.w)
        self.hit_box2 = pygame.Rect(x2, y2, self.h, self.h)
        x2 = int(self.h/2)
        y2 = int(self.h / 2)
    def draw(self,screen):
        pygame.draw.rect(screen, (255, 13, 67), self.hit_box, border_radius=int(self.w / 2))
        pygame.draw.rect(screen, (200, 0, 0), self.hit_box2, border_radius=int(self.w / 2))


running = True
a = Krator(250,250)
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    a.draw(screen)
    pygame.display.update()
