__author__ = 'josiah'
import pygame
import keyboardManager

def getEventProcessQueue():
    eventProcessQueue = []
    events = pygame.event.get()
    keydownEvents = []
    for event in events:
        if event.type is pygame.KEYDOWN:
            keydownEvents.append(event)
    eventProcessQueue += (keyboardManager.getKeyboardProcessQueue(keydownEvents))
    return eventProcessQueue
