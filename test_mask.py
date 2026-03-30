import pygame as pg
from pygame.math import Vector2

pg.init()
screen = pg.display.set_mode((800, 600))
clock = pg.time.Clock()
BG_COLOR = pg.Color(30, 90, 0)

a = pg.Rect(10, 10, 100, 100)
b = pg.Rect(120, 10, 100, 100)
a1 = (255, 255, 255, 100)
b1 = (255, 255, 255)
alpha = 0
fog = pg.Surface((800, 600), pg.SRCALPHA)
done = False
seconds = 60
fps = 10
timer = 0
day = 1 * seconds * fps
night = 1 * seconds * fps
sun_move = 1 * seconds * fps
past_time = 'night'
curent_time = 'day'
while not done:
    timer += 1
    print((day-timer)//60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

    if curent_time == 'day':
        if timer > day:
            timer = 0
            curent_time = 'sun_move'
    elif curent_time == 'sun_move':
        if timer > sun_move:
            timer = 0
            if past_time == 'day':
                past_time = 'night'
                curent_time = 'day'
            if past_time == 'night':
                past_time = 'day'
                curent_time = 'night'
        if past_time == 'day':
            alpha -= 200 / sun_move
        if past_time == 'night':
            alpha += 200 / sun_move
        if alpha < 0:
            alpha = 0
        elif alpha > 200:
            alpha = 200
        print(alpha)
    elif curent_time == 'night':
        if timer > night:
            timer = 0
            curent_time = 'sun_move'
    screen.fill(BG_COLOR)
    pg.draw.rect(screen, a1, a)
    pg.draw.rect(screen, b1, b)
    fog.fill((10, 10, 10, int(alpha)))
    screen.blit(fog, (0, 0))
    pg.display.flip()
    clock.tick(60)

pg.quit()
