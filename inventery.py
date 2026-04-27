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
     def draw(self,screen):
         screen.blit(self.surface,self.rect)



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



