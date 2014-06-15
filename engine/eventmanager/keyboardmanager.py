__author__ = 'josiah'
import sys
import pygame
from engine.objectmanager import objectmanager
from engine.gfxmanager import gfxmanager
from engine.physicsmanager import physicsmanager

movement_keys = [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d]

def run_editor_keyboard_processes():
    keys = pygame.key.get_pressed()
    if movement_key_pressed(keys) and not keys[pygame.K_LCTRL]:
        vector = [((keys[pygame.K_a]-keys[pygame.K_d])*4), ((keys[pygame.K_w]-keys[pygame.K_s])*4)]
        gfxmanager.move_screen(vector)

def run_keyboard_processes(keydown_events):
    keys = pygame.key.get_pressed()
    player = objectmanager.get_player()

    # Handling for HELD keys
    if keys[pygame.K_q]:
        sys.exit()
    if movement_key_pressed(keys):
        if player is not None:
            vector = [(keys[pygame.K_d]-keys[pygame.K_a])*player.run_velocity, 0]
            player.apply_vel(vector)

    # Handling for PRESSED keys
    for event in keydown_events:
        if event.key is pygame.K_SPACE:
            if player is not None:
                physicsmanager.jump(player)

def movement_key_pressed(keys):
    for key in movement_keys:
        if keys[key]:
            return True
