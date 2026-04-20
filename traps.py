import pygame
import random


class Trap:
    def __init__(self, x, y):
        self.w = random.randint(80, 160)
        self.color = (255, 0, 0, 15)
        self.hit_box = pygame.Rect(x, y, self.w, self.w)
        self.hit_box.center = (x, y)
        self.damage = random.random()
        self.surface = pygame.Surface((self.hit_box.width, self.hit_box.width), pygame.SRCALPHA)
        self.surface.fill(self.color)

    def draw(self, screen):
        # pygame.draw.rect(screen, self.color, self.hit_box)
        screen.blit(self.surface, self.hit_box.topleft)


    def save(self):
        data = {'pos': self.hit_box.center,
                'width': self.hit_box.width,
                'color': self.color,
                'damage': self.damage
                }
        return data

    def load(self, data):
        x, y = data.get('pos')
        self.w = data.get('width')
        self.hit_box = pygame.Rect(x, y, self.w, self.w)
        self.hit_box.center = (x, y)
        self.color = data.get('color')
        self.damage = data.get('damage')

if __name__ == '__main__':
    import pygame

    S_W = 500
    S_H = 500
    screen = pygame.display.set_mode((S_W, S_H))
    running = True
    a = Traps(250, 250)
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill('white')
        a.draw(screen)
        pygame.display.update()




