import pygame as pg
from pygame.math import Vector2


pg.init()
screen = pg.display.set_mode((800, 600))
clock = pg.time.Clock()
BG_COLOR = pg.Color(30, 90, 0)

a = pg.Rect(10,10,100,100)
b = pg.Rect(120,10,100,100)
a1 = (255,255,255,100)
b1 = (255,255,255)
f = 0
fog = pg.Surface((800, 600), pg.SRCALPHA)
done = False
timer = 0
while not done:
    timer+=1
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True


    f+=clock.get_rawtime()
    print(f,clock.get_rawtime())



    screen.fill(BG_COLOR)
    pg.draw.rect(screen,a1,a)
    pg.draw.rect(screen,b1,b)
    fog.fill((10,10,10,100))
    screen.blit(fog,(0,0))
    pg.display.flip()
    clock.tick(60)

pg.quit()