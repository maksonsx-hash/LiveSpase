import pygame.font

from utils import load_settings,save_settings
import os

pygame.font.init()

if os.path.exists('Save.json'):
    print("Файл/директория существует")
    data = load_settings()
    SCREEN_INDEX = data.get('SCREEN_INDEX')
    BACKGROUND_INDEX = data.get('BACKGROUND_INDEX')
else:
    print("Не существует")
    SCREEN_INDEX = 3
    BACKGROUND_INDEX = 0
    data = {'SCREEN_INDEX':3,
            'BACKGROUND_INDEX':0}
    save_settings(data)

font = pygame.font.SysFont('Comic Sans', 18)
SCREEN_SIZE = [(600, 600), (700, 700), (720, 720), (800, 800), (1280, 720)]
S_W, S_H = SCREEN_SIZE[SCREEN_INDEX]
