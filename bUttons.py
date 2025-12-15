import pygame
from config import font


class Button:
    def __init__(self, x, y, width, height,color, text):
        self.rect = pygame.Rect(x-width/2, y-height/2, width, height)
        self.color = color
        self.standart_color = color
        self.active_color = 'white'
        self.text_img = font.render(text, True, (0, 0, 0))
        self.text_rect = self.text_img.get_rect()
        self.text_rect.center = self.rect.center
        self.pressed = False
        self.action_ = False
    def draw(self, screen):
        pygame.draw.rect(screen,self.color, self.rect,border_radius=10)
        screen.blit(self.text_img, self.text_rect)
    def update(self,screen):
        self.change_color()
        self.draw(screen)
        self.action()

    def change_color(self):
        mouse_x, mouse_y= pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_x, mouse_y):
            self.color = self.active_color
        else:
            self.color =  self.standart_color
    def action(self):

        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_x, mouse_y):
            if_pressed = pygame.mouse.get_pressed()
            if if_pressed[0] == True:
                self.pressed = True
            else:
                self.pressed = False
        else:
            self.pressed = False








