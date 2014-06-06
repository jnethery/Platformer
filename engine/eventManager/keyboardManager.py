__author__ = 'josiah'
import pygame
from engine.processManager import process
from engine.objectManager import objectManager

movementKeys = [pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d]

def getProcess(keys):
    if keys[pygame.K_q]:
        return process.getProcess('sys', 'exit', None)
    if movementKeyPressed(keys):
        params = {}
        params['object'] = objectManager.objectSet['player'][0]
        params['vector'] = [keys[pygame.K_d]-keys[pygame.K_a], keys[pygame.K_s]-keys[pygame.K_w]]
        return process.getProcess('physics', 'move', params)
    else:
        return process.getProcess(None, None, None)

def movementKeyPressed(keys):
    for key in movementKeys:
        if keys[key]:
            return True
