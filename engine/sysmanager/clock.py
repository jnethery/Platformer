__author__ = 'josiah'
import pygame
from engine import config

clock = pygame.time.Clock()

def get_fps():
    if clock.get_fps() != 0:
        return clock.get_fps()
    else:
        return config.physics['fps']