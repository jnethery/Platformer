__author__ = 'josiah'
import sys
import pygame
import keyboardmanager
from engine.editor import editor
from engine.procmanager import process

def run_event_processes():
    events = pygame.event.get()
    keydown_events = []
    for event in events:
        if event.type is pygame.KEYDOWN:
            keydown_events.append(event)
    keyboardmanager.run_keyboard_processes(keydown_events)

def run_editor_event_processes():
    events = pygame.event.get()
    for event in events:
        if event.type is pygame.KEYDOWN:
            if event.key is pygame.K_q:
                sys.exit()
            if event.key is pygame.K_s and event.mod == 64:
                print 'Saving level...'
                editor.save_editor_level()
    keyboardmanager.run_editor_keyboard_processes()

    # Mouse stuff
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()
    editor.show_editor_cursor(mouse_pos)
    if mouse_pressed[0] == 1:
        editor.add_object(mouse_pos)
    if mouse_pressed[2] == 1:
        editor.delete_object(mouse_pos)
