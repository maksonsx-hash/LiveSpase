import pygame


class MenuKrator:
    def __init__(self, name, timer, kolvo):
        self.name = name
        self.timer = timer
        self.kolvo = kolvo
        self.color = (0, 0, 0, 150)
        self.color2 = (0, 0, 0, 200)
        self.rect = pygame.Rect(200, 200, 350, 200)
        self.surface = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        self.surface.fill(self.color)
        self.gap = 5
        self.name_surface = pygame.Surface(((self.rect.width - self.gap * 3) / 2, (self.rect.height - self.gap * 3) / 2),
                                           pygame.SRCALPHA)
        self.name_surface.fill(self.color)
        self.kolvo_surface = pygame.Surface(((self.rect.width - self.gap * 3) / 2, (self.rect.height - self.gap * 3) / 2),
                                            pygame.SRCALPHA)
        self.timer_surface = pygame.Surface(((self.rect.width - self.gap * 2), (self.rect.height - self.gap * 3) / 2),
                                            pygame.SRCALPHA)

    def draw(self, screen):
        self.surface.blit(self.name_surface,(self.gap,self.gap))
        screen.blit(self.surface, self.rect)


if __name__ == '__main__':
    import pygame

    S_W, S_H = (1280, 720)
    screen = pygame.display.set_mode((S_W, S_H))
    running = True
    a = MenuKrator('золото', 10, 50)
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255, 255, 255))
        a.draw(screen)
        pygame.display.update()
