__author__ = 'josiah'
import sys, pygame, cProfile
from engine.levelManager import levelManager
from engine.processManager import processManager
from engine.systemManager import clock
from engine import config

pygame.init()
levelManager.loadLevel('001')

engineState = 0
profileState = 1
showFps = 0

#game loop
while engineState is 0:
    processManager.runProcessQueue(engineState)
    clock.clock.tick(config.physics['fps'])
    if profileState is 1 and clock.clock.get_fps() < 30 and pygame.time.get_ticks() > 1000:
        cProfile.run('processManager.runProcessQueue(0)', None, sort=1)
        sys.exit()
    if showFps is 1:
        print clock.clock.get_fps()

#level editor loop
while engineState is 1:
    processManager.runProcessQueue(engineState)
    clock.clock.tick(config.physics['fps'])
