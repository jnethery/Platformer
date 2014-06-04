__author__ = 'josiah'
import pygame
from processManager import processManager
pygame.init()

while (True):
    processManager.runProcessQueue()