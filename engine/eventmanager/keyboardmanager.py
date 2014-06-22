__author__ = 'josiah'
import sys
import pygame
from engine import config
from engine.editor import editor
from engine.objectmanager import objectmanager
from engine.gfxmanager import gfxmanager
from engine.physicsmanager import physicsmanager

movement_keys = [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d]

def run_editor_keyboard_processes(keydown_events):
    keys = pygame.key.get_pressed()

    # Handling for HELD keys
    if movement_key_pressed(keys) and keys[pygame.K_LSHIFT]:
        vector = [((keys[pygame.K_a]-keys[pygame.K_d])*32), ((keys[pygame.K_w]-keys[pygame.K_s])*32)]
        gfxmanager.move_screen(vector)

    for event in keydown_events:
        if event.key is pygame.K_q:
            sys.exit()
        elif event.key is pygame.K_s and event.mod == 64:
            print 'Saving level...'
            editor.save_editor_level()
        elif event.key is pygame.K_a or pygame.K_d and event.mod != 1:
            tile_size = config.physics['tile']['tile_size']
            vector = [((keys[pygame.K_a]-keys[pygame.K_d])*tile_size), ((keys[pygame.K_w]-keys[pygame.K_s])*tile_size)]
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
