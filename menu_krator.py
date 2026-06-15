import pygame
from config import font
from bUttons import Button


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
        self.name_image = font.render(self.name, True, 'white')
        self.timer_image = font.render(str(self.timer), True, 'white')
        self.kolvo_image = font.render(str(self.kolvo), True, 'white')

        self.click_rect = Button(self.rect.centerx, self.rect.centery, 100, 50, 'blue', 'Забрать' )
        self.name_rect = pygame.Rect(
            self.gap, self.gap,
            (self.rect.width - self.gap * 3) / 2, (self.rect.height - self.gap * 3) / 2)
        self.kolvo_rect = pygame.Rect(
            self.gap * 2 + self.name_rect.width, self.gap,
            (self.rect.width - self.gap * 3) / 2, (self.rect.height - self.gap * 3) / 2)
        self.timer_rect = pygame.Rect(
            self.gap, self.gap * 2 + self.name_rect.height,
            (self.rect.width - self.gap * 2), (self.rect.height - self.gap * 3) / 2)
        self.timer_image_rect = self.timer_image.get_rect()
        self.timer_image_rect.center = self.timer_rect.center
        self.name_image_rect = self.name_image.get_rect()
        self.name_image_rect.center = self.name_rect.center
        self.kolvo_image_rect = self.kolvo_image.get_rect()
        self.kolvo_image_rect.center = self.kolvo_rect.center
    def draw(self, screen,now_time):
        pygame.draw.rect(self.surface, self.color2, self.name_rect)
        pygame.draw.rect(self.surface, self.color2, self.kolvo_rect)
        pygame.draw.rect(self.surface, self.color2, self.timer_rect)
        self.surface.blit(self.name_image, self.name_image_rect)
        self.surface.blit(self.kolvo_image, self.kolvo_image_rect)
        self.surface.blit(self.timer_image, self.timer_image_rect)
        screen.blit(self.surface, self.rect)
        self.click_rect.update(screen)
        if self.click_rect.action_:
            if self.kolvo!=0:
                self.time_resurs = now_time
            self.kolvo = 0

    def update_timer(self):
        if self.kolvo != 0:
            self.timer = 10

        else:
            self.timer-=1
            if self.timer == 0:
                self.timer = 0
                self.kolvo = 50




        self.timer_image = font.render(str(self.timer), True, 'white')
        self.kolvo_image = font.render(str(self.kolvo), True, 'white')


if __name__ == '__main__':
    import pygame

    S_W, S_H = (1280, 720)
    screen = pygame.display.set_mode((S_W, S_H))
    running = True
    a = MenuKrator('золото', 10, 50)
    clock = pygame.time.Clock()
    fps = 120
    timer = 0
    past_time = 0
    while running:
        timer += clock.tick(fps)
        now_time = timer//1000
        if now_time > past_time:
            past_time = now_time
            a.update_timer()
            print(now_time, a.timer)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255, 255, 255))
        a.draw(screen)
        pygame.display.update()
