import pygame


class Button:
    def __init__(self, x, y, width, height,color):
        self.rect = pygame.Rect(x-width/2, y-height/2, width, height)
        self.color = color
        self.standart_color = color
        self.active_color = 'white'
    def draw(self, screen):
        pygame.draw.rect(screen,self.color, self.rect,border_radius=10)
    def update(self,screen):
        self.change_color()
        self.draw(screen)

    def change_color(self):
        mouse_x, mouse_y= pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_x, mouse_y):
            self.color = self.active_color
        else:
            self.color =  self.standart_color


