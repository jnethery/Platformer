__author__ = 'josiah'
import pygame
import keyboardmanager
from engine.editor import editor
from engine.procmanager import process

def get_event_process_queue():
    event_process_queue = []
    events = pygame.event.get()
    keydown_events = []
    for event in events:
        if event.type is pygame.KEYDOWN:
            keydown_events.append(event)
    event_process_queue += (keyboardmanager.get_keyboard_process_queue(keydown_events))
    return event_process_queue

def get_editor_event_process_queue():
    event_process_queue = []
    events = pygame.event.get()
    for event in events:
        if event.type is pygame.KEYDOWN:
            if event.key is pygame.K_q:
                event_process_queue.append(process.get_process('sys', 'exit', None))
            if event.key is pygame.K_s and event.mod == 64:
                print 'Saving level...'
                event_process_queue.append(process.get_process('editor', 'save', None))
    event_process_queue += (keyboardmanager.get_editor_keyboard_process_queue())

    # Mouse stuff
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()
    editor.show_editor_cursor(mouse_pos)
    if mouse_pressed[0] == 1:
        event_process_queue.append(editor.add_object(mouse_pos))
    if mouse_pressed[2] == 1:
        event_process_queue.append(editor.delete_object(mouse_pos))
    return event_process_queue
