__author__ = 'josiah'
import pygame
from engine.procmanager import process
from engine.objectmanager import objectmanager

movement_keys = [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d]

def get_editor_keyboard_process_queue():
    process_list = []
    keys = pygame.key.get_pressed()
    if movement_key_pressed(keys) and not keys[pygame.K_LCTRL]:
        params = {}
        params['vector'] = [((keys[pygame.K_a]-keys[pygame.K_d])*4), ((keys[pygame.K_w]-keys[pygame.K_s])*4)]
        process_list.append(process.get_process('gfx', 'move_screen', params))
    return process_list

def get_keyboard_process_queue(keydown_events):
    process_list = []
    keys = pygame.key.get_pressed()

    # Handling for HELD keys
    if keys[pygame.K_q]:
        process_list.append(process.get_process('sys', 'exit', None))
    if movement_key_pressed(keys):
        player = objectmanager.get_player()
        if player is not None:
            params = {}
            params['object'] = player
            params['vector'] = [(keys[pygame.K_d]-keys[pygame.K_a])*params['object'].run_velocity, 0]
            process_list.append(process.get_process('physics', 'apply_velocity', params))

    # Handling for PRESSED keys
    for event in keydown_events:
        if event.key is pygame.K_SPACE:
            params = {}
            params['object'] = objectmanager.get_player()
            process_list.append(process.get_process('physics', 'jump', params))

    return process_list

def movement_key_pressed(keys):
    for key in movement_keys:
        if keys[key]:
            return True
