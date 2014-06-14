__author__ = 'josiah'
import pygame
from engine.levelManager import levelManager
from engine.processManager import processManager
from engine.systemManager import clock
from engine import config

pygame.init()
levelManager.loadLevel('001')

engineState = 0

#game loop
while engineState is 0:
    processManager.runProcessQueue(engineState)
    clock.clock.tick(config.physics['fps'])

#level editor loop
while engineState is 1:
    processManager.runProcessQueue(engineState)
    clock.clock.tick(config.physics['fps'])
