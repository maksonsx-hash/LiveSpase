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
        self.hp_now = pygame.Rect(0,0,self.hp*2-10,25)
        self.hp_now.left = self.base_hp.left+5
        self.hp_now.centery = self.base_hp.centery
        self.stamina_now = pygame.Rect(0, 0, self.stamina * 2 - 10, 25)
        self.stamina_now.left = self.base_stamina.left + 5
        self.stamina_now.centery = self.base_stamina.centery

        

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.hit_box)
        pygame.draw.rect(surface, (0,0,0), self.base_hp)
        pygame.draw.rect(surface, (0,0,0), self.base_stamina)
        pygame.draw.rect(surface,'red',self.hp_now)
        pygame.draw.rect(surface, 'blue', self.stamina_now)

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
    def change_hp(self,amount,get=True):
        if get:
            print('получаем ', amount)
            self.hp += amount
            if self.hp > self.max_hp:
                self.hp = self.max_hp
        else:
            print('теряем', amount)
            self.hp -= amount
            if self.hp < 0:
                self.hp = 0

        self.hp_now = pygame.Rect(0, 0, round(self.hp) * 2 - 10, 25)
        self.hp_now.left = self.base_hp.left + 5
        self.hp_now.centery = self.base_hp.centery

    def change_stamina(self,amount,get=True):

        if get:

            self.stamina += amount
            if  self.stamina > self.max_stamina:
                self.stamina = self.max_stamina
        else:

            self.stamina -= amount
            if  self.stamina < 0:
                self.stamina =  0

        self.stamina_now = pygame.Rect(0, 0, self.stamina * 2 - 10, 25)
        self.stamina_now.left = self.base_stamina.left + 5
        self.stamina_now.centery = self.base_stamina.centery


