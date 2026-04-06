import pygame
import random
from config import S_W,S_H

class Player:
    def __init__(self, x, y):

        self.hit_box = pygame.Rect(x, y, 16, 24)
        self.speed = 5
        self.hp = 100
        self.stamina = 100
        self.max_hp = 100
        self.max_stamina = 100
        self.color = (0, 0, 0)
        self.base_hp = pygame.Rect(0,0,self.max_hp*2,30)
        self.base_hp.topright = (S_W-10,10)
        self.base_stamina = pygame.Rect(0, 0, self.max_stamina * 2, 30)
        self.base_stamina.topright = (S_W - 10, 45)
        

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.hit_box)
        pygame.draw.rect(surface, (255,0,0), self.base_hp)
        pygame.draw.rect(surface, (0,0,0), self.base_stamina)
        
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
