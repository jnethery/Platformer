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
    editor.showEditorCursor(pygame.mouse.get_pos())
    events = pygame.event.get()
    for event in events:
        if event.type is pygame.KEYDOWN:
            if event.key is pygame.K_q:
                eventProcessQueue.append(process.getProcess('sys', 'exit', None))
            if event.key is pygame.K_s and event.mod == 64:
                print 'Saving level...'
                eventProcessQueue.append(process.getProcess('editor', 'save', None))
        if event.type is pygame.MOUSEBUTTONDOWN:
            if event.button is 1:
                eventProcessQueue.append(editor.addObject(event.pos))
            if event.button is 3:
                eventProcessQueue.append(editor.deleteObject(event.pos))
    eventProcessQueue += (keyboardManager.getEditorKeyboardProcessQueue())
    return eventProcessQueue
