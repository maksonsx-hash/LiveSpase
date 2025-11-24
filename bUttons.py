import pygame


class Button:
    def __init__(self, x, y, width, height,):
        self.rect = pygame.Rect(x-width/2, y-height/2, width, height)

    def draw(self, screen):
        pygame.draw.rect(screen, 'red', self.rect)
