import random
import pygame
from menu_krator import MenuKrator
from bUttons import Button
from player import Player

NAME_MAPPING ={'gold':{'name':'золотой','value_min':10,'value_max':20,'timer':300},
               'orange':{'name':'железный','value_min':15,'value_max':30,'timer':200},}



class Krator:
    def __init__(self, x, y, type_):
        self.invisible = False if type_ else True
        self.w = random.randint(80, 160)
        self.type_ = type_
        self.chose_color(type_)
        self.color = (self.a, self.b, self.c)
        self.hit_box = pygame.Rect(x, y, self.w, self.w)
        self.hit_box.center = (x, y)
        self.random_value_choice(type_)
        self.show_menu = False
        self.menu_krator = MenuKrator(self.name,self.timer,self.value)
        self.button = Button(self.hit_box.centerx,self.hit_box.centery,70,40,'blue','открыть')


    def random_value_choice(self,type_):
        if type_ in NAME_MAPPING.keys():
            temp_dict = NAME_MAPPING.get(type_)
            self.timer = temp_dict.get('timer')
            self.name =temp_dict.get('name')
            self.value = random.randint(temp_dict.get('value_min'), temp_dict.get('value_max'))

        else:
            self.value = 0
            self.timer = 0
            self.name = '0'
    def draw(self, screen, player_hit_box,now_time):
        if not self.invisible:

            # pygame.draw.rect(screen, (255, 13, 67), self.hit_box, border_radius=int(self.w / 2))
            # pygame.draw.rect(screen, (200, 0, 0), self.hit_box2, border_radius=int(self.w / 2))
            pygame.draw.circle(screen, self.a, self.hit_box.center, self.hit_box.width / 2)
            pygame.draw.circle(screen, self.b, self.hit_box.center, self.hit_box.width / 3)
            pygame.draw.circle(screen, self.c, self.hit_box.center, self.hit_box.width / 5)
            if self.hit_box.colliderect (player_hit_box):
                self.button.update(screen)
                if self.button.action_:
                   self.show_menu = True
                if self.show_menu:
                    self.menu_krator.draw(screen,now_time)
            else:
                self.show_menu = False
    def chose_color(self, type_):
        if type_ == 'orange':
            self.a = random.randint(200, 255), random.randint(100, 165), random.randint(0, 50)
            self.b = random.randint(200, 255), random.randint(60, 76), random.randint(0, 10)
            self.c = random.randint(200, 255), random.randint(140, 160), random.randint(0, 40)
        elif type_ == 'gold':
            self.a = random.randint(230, 255), random.randint(200, 220), random.randint(0, 10)
            self.b = random.randint(200, 240), random.randint(200, 221), random.randint(100, 140)
            self.c = random.randint(200, 220), random.randint(130, 150), random.randint(30, 50)
        else:
            self.a,self.b,self.c = 0,0,0
    def save(self):
        data = {'type_': self.type_,
                'pos': self.hit_box.center,
                'width': self.hit_box.width,
                'color': self.color,
                'invisible':self.invisible,
                'name':self.name,
                'value':self.value,
                'timer':self.timer}
        return data

    def load(self, data):
        self.type_ = data.get('type_')
        x, y = data.get('pos')
        self.w = data.get('width')
        self.hit_box = pygame.Rect(x, y, self.w, self.w)
        self.hit_box.center = (x, y)
        self.color = data.get('color')
        self.invisible = data.get('invisible')
        self.timer = data.get('timer')
        self.value = data.get('value')
        self.name = data.get('name')
        self.a, self.b, self.c = self.color
    def __str__(self):
        text = f'''тип:{self.type_}, цвет:{self.color}, место:{self.hit_box.center}, прозрачность:{self.invisible}'''
        return text


if __name__ == '__main__':
    import pygame

    S_W = 500
    S_H = 500
    player = Player(S_W / 2, S_H / 2)
    screen = pygame.display.set_mode((S_W, S_H))
    running = True
    a = Krator(250, 250, 'gold')
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255, 255, 255))
        a.draw(screen, player.hit_box)
        player.draw(screen)
        player.move()
        pygame.display.update()

