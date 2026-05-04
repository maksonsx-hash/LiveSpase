from config import font

IMAGE_MAP = {'железо': 'images/res/iron.png',
             'золото': 'images/res/gold.png'}


class Inventory:
    def __init__(self):
        self.items = [{'name': 'железо', 'value': 10},
                      {'name': 'золото', 'value': 200},
                      {'name': 'медь', 'value': 50},
                      {'name': 'серебро', 'value': 15},
                      {'name': 'германий', 'value': 5}, ]
        self.load_image()
        self.color = (0, 0, 0, 150)
        self.rect = pygame.Rect(20, 20, S_W / 3, S_H - 40)
        self.surface = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        self.surface.fill(self.color)
        self.row_surface = pygame.Surface((self.rect.width, 20), pygame.SRCALPHA)
        self.row_surface.fill(self.color)

    def load_image(self):
        for index, item in enumerate(self.items):
            item_path = IMAGE_MAP.get(item.get("name"))
            if item_path:
                image = pygame.image.load(item_path)
                image = pygame.transform.smoothscale(image,(20,20))
            else:
                image = font.render('none', True, (255, 255, 255))
            self.items[index]['image'] = image
    def draw(self, screen):
        screen.blit(self.surface, self.rect)
        for y, item in enumerate(self.items):
            gap = 2
            if y == 0:
                pass
            else:
                y = y * (gap + 20)
            print(y)
            screen.blit(self.row_surface, (self.rect.x, self.rect.y + y))

            text_img = font.render(item.get('name'), True, (255, 255, 255))
            text_img_rect = text_img.get_rect()
            text_img_rect.center = (self.rect.centerx, self.rect.top + y + 8)
            screen.blit(text_img, text_img_rect)

            icone_img = item.get('image')
            icone_img_rect = icone_img.get_rect()
            icone_img_rect.centery = text_img_rect.centery+2
            icone_img_rect.x = self.rect.x + 5
            screen.blit(icone_img, icone_img_rect)


if __name__ == '__main__':
    import pygame

    S_W, S_H = (1280, 720)
    screen = pygame.display.set_mode((S_W, S_H))
    running = True
    a = Inventory()
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((255, 255, 255))
        a.draw(screen)
        pygame.display.update()
