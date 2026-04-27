class Inventory:
     def __init__(self):
         self.items = [{'name':'железо','value':10},
                       {'name':'золото','value':200},
                       {'name':'медь','value':50},
                       {'name':'серебро','value':15},
                       {'name':'германий','value':5},]
         self.color = (0,0,0,150)
         self.rect = pygame.Rect(20,20,S_W/3,S_H-40)
         self.surface = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
         self.surface.fill(self.color)
         self.row_surface = pygame.Surface((self.rect.width, 20), pygame.SRCALPHA)
         self.row_surface.fill(self.color)
     def draw(self,screen):
         screen.blit(self.surface,self.rect)
         for y, item in enumerate(self.items):
             gap = 2
             if y == 0:
                 pass
             else:
                 y = y * (gap + 20)
             print(y)
             screen.blit(self.row_surface, (self.rect.x, self.rect.y + y))



if __name__ == '__main__':
    import pygame

    S_W,S_H = (1280, 720)
    screen = pygame.display.set_mode((S_W, S_H))
    running = True
    a = Inventory()
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255,255,255))
        a.draw(screen)
        pygame.display.update()



