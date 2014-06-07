__author__ = 'josiah'
import pygame
from engine.processManager import process
from engine.objectManager import objectManager

movementKeys = [pygame.K_a, pygame.K_d]

def getKeyboardProcessQueue(keydownEvents):
    processList = []
    keys = pygame.key.get_pressed()

    # Handling for HELD keys
    if keys[pygame.K_q]:
        processList.append(process.getProcess('sys', 'exit', None))
    if movementKeyPressed(keys):
        params = {}
        params['object'] = objectManager.objectSet['player'][0]
        params['vector'] = [(keys[pygame.K_d]-keys[pygame.K_a])*params['object'].run_velocity, 0]
        processList.append(process.getProcess('physics', 'applyVelocity', params))

    # Handling for PRESSED keys
    for event in keydownEvents:
        if event.key is pygame.K_SPACE:
            params = {}
            params['object'] = objectManager.objectSet['player'][0]
            processList.append(process.getProcess('physics', 'jump', params))

    return processList

def movementKeyPressed(keys):
    for key in movementKeys:
        if keys[key]:
            return True
