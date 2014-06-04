__author__ = 'josiah'
import pygame
import keyboardManager

def getEventProcessQueue():
    eventProcessQueue = []
    events = pygame.event.get()
    keys = pygame.key.get_pressed()
    for event in events:
        pass
    eventProcessQueue.append(keyboardManager.getProcess(keys))
    return eventProcessQueue
