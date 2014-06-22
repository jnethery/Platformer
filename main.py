__author__ = 'josiah'
import sys
import pygame
import cProfile
from engine.levelmanager import levelmanager
from engine.procmanager import procmanager
from engine.gfxmanager import gfxmanager
from engine.sysmanager import clock
from engine import config

engine_state = 0
profile_state = False
show_fps = False

#initialize
pygame.init()
levelmanager.load_level('000')
gfxmanager.init_screen(engine_state)

#game loop
while engine_state == 0:
    procmanager.run_processes(engine_state)
    clock.clock.tick(config.physics['fps'])
    if profile_state and clock.clock.get_fps() < 55 and pygame.time.get_ticks() > 1000:
        cProfile.run('procmanager.run_processes(0)', None, sort = 1)
        sys.exit()
    if show_fps:
        print clock.clock.get_fps()

#level editor loop
while engine_state == 1:
    procmanager.run_processes(engine_state)
    clock.clock.tick(config.physics['fps'])
