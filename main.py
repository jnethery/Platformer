__author__ = 'josiah'
import pygame
from engine.processManager import processManager
pygame.init()

while (True):
    processManager.runProcessQueue()