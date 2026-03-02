import random

import pygame

S_W = 500
S_H = 500
screen = pygame.display.set_mode((S_W, S_H))


class Krator:
    def __init__(self, x, y, type_):
        self.w = random.randint(80, 160)
        self.type_ = type_
        self.chose_color(type_)
        self.color = (self.a, self.b, self.c)
        self.hit_box = pygame.Rect(x, y, self.w, self.w)
        self.hit_box.center = (x, y)

    def draw(self, screen):
        # pygame.draw.rect(screen, (255, 13, 67), self.hit_box, border_radius=int(self.w / 2))
        # pygame.draw.rect(screen, (200, 0, 0), self.hit_box2, border_radius=int(self.w / 2))
        pygame.draw.circle(screen, self.a, self.hit_box.center, self.hit_box.width / 2)
        pygame.draw.circle(screen, self.b, self.hit_box.center, self.hit_box.width / 3)
        pygame.draw.circle(screen, self.c, self.hit_box.center, self.hit_box.width / 5)

    def chose_color(self, type_):
        if type_ == 'orange':
            self.a = random.randint(200, 255), random.randint(0, 50), random.randint(50, 100)
            self.b = random.randint(200, 255), random.randint(0, 10), random.randint(70, 100)
            self.c = random.randint(200, 255), random.randint(90, 100), random.randint(50, 100)
        if type_ == 'gold':
            self.a = random.randint(100, 155), random.randint(0, 50), random.randint(50, 100)
            self.b = random.randint(100, 155), random.randint(0, 10), random.randint(70, 100)
            self.c = random.randint(100, 155), random.randint(90, 100), random.randint(50, 100)

    def save(self):
        data = {'type_': self.type_,
                'pos': self.hit_box.center,
                'width': self.hit_box.width,
                'color': self.color}
        return data

    def load(self, data):
        self.type_ = data.get('type_')
        x, y = data.get('pos')
        self.w = data.get('width')
        self.hit_box = pygame.Rect(x, y, self.w, self.w)
        self.hit_box.center = (x, y)
        self.color = data.get('color')
        self.a, self.b, self.c = self.color


running = True
a = Krator(250, 250, 'gold')
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    a.draw(screen)
    pygame.display.update()
