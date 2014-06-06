__author__ = 'josiah'
import pygame
from engine.processManager import processManager
from engine.systemManager import clock
from engine import config

pygame.init()

while (True):
    processManager.runProcessQueue()
    clock.clock.tick(config.physics['fps']) #the game is limited to 60 FPS
