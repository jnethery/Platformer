__author__ = 'josiah'
import pygame
import keyboardManager
from engine.editor import editor
from engine.processManager import process

def getEventProcessQueue():
    eventProcessQueue = []
    events = pygame.event.get()
    keydownEvents = []
    for event in events:
        if event.type is pygame.KEYDOWN:
            keydownEvents.append(event)
    eventProcessQueue += (keyboardManager.getKeyboardProcessQueue(keydownEvents))
    return eventProcessQueue

def getEditorEventProcessQueue():
    eventProcessQueue = []
    events = pygame.event.get()
    for event in events:
        if event.type is pygame.KEYDOWN:
            if event.key is pygame.K_q:
                eventProcessQueue.append(process.getProcess('sys', 'exit', None))
            if event.key is pygame.K_s and event.mod == 64:
                print 'Saving level...'
                eventProcessQueue.append(process.getProcess('editor', 'save', None))
    eventProcessQueue += (keyboardManager.getEditorKeyboardProcessQueue())

    # Mouse stuff
    mousePosition = pygame.mouse.get_pos()
    mousePressed = pygame.mouse.get_pressed()
    editor.showEditorCursor(mousePosition)
    if mousePressed[0] == 1:
        eventProcessQueue.append(editor.addObject(mousePosition))
    if mousePressed[2] == 1:
        eventProcessQueue.append(editor.deleteObject(mousePosition))
    return eventProcessQueue
