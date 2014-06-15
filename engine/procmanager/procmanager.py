__author__ = 'josiah'
from engine.eventmanager import eventmanager
from engine.gfxmanager import gfxmanager
from engine.physicsmanager import physicsmanager
from engine.objectmanager import objectmanager

def run_editor_processes():
    eventmanager.run_editor_event_processes()
    gfxmanager.run_editor_gfx_processes()

def run_game_processes():
    proc_queue = []
    objectmanager.set_physics_objects()
    physicsmanager.process_physics()
    objectmanager.killObjects()
    eventmanager.run_event_processes()
    gfxmanager.run_gfx_processes()
    return proc_queue

def run_processes(engine_state):
    if engine_state is 0:
        run_game_processes()
    if engine_state is 1:
        run_editor_processes()
