import sys

import pygame

def check_events():
    """ Отслеживание событий клавиатуры и мыши"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()