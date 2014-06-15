__author__ = 'josiah'
import sys
from engine.eventmanager import eventmanager
from engine.gfxmanager import gfxmanager
from engine.physicsmanager import physicsmanager
from engine.objectmanager import objectmanager
from engine.editor import editor

def get_editor_proc_queue():
    proc_queue = []
    proc_queue += eventmanager.get_editor_event_process_queue()
    proc_queue += gfxmanager.get_editor_graphics_process_queue()
    return proc_queue

def get_proc_queue():
    proc_queue = []
    objectmanager.set_physics_objects()
    physicsmanager.process_physics()
    objectmanager.killObjects()
    proc_queue += eventmanager.get_event_process_queue()
    proc_queue += gfxmanager.get_graphics_process_queue()
    return proc_queue

def run_proc_queue(engine_state):
    if engine_state is 0:
        proc_queue = get_proc_queue()
    if engine_state is 1:
        proc_queue = get_editor_proc_queue()
    for process in proc_queue:
        system = process['system']
        method = process['method']
        params = process['params']
        if system is 'sys':
            run_sys_proc(method, params)
        if system is 'physics':
            run_physics_proc(method, params)
        if system is 'gfx':
            run_gfx_proc(method, params)
        if system is 'sound':
            pass
        if system is 'editor':
            run_editor_proc(method, params)
        else:
            pass

def run_editor_proc(method, params):
    if method is 'save':
        editor.save_level()
    if method is 'add_object':
        object = params['object']
        objectmanager.object_sets['level'].append(object)
    if method is 'delete_object':
        object = params['object']
        type = params['type']
        if type is not None:
            objectmanager.object_sets[type].remove(object)

def run_sys_proc(method, params):
    if method is 'exit':
        sys.exit()
    else:
        pass

def run_physics_proc(method, params):
    if method is 'apply_velocity':
        object = params['object']
        vector = params['vector']
        physicsmanager.apply_vel(object, vector)
    if method is 'jump':
        object = params['object']
        physicsmanager.jump(object)

def run_gfx_proc(method, params):
    if method is 'move_screen':
        gfxmanager.move_screen(params['vector'])
    if method is 'fill':
        gfxmanager.fill_screen()
    if method is 'flip':
        gfxmanager.flip_screen()
    if method is 'blit':
        gfxmanager.blit(params['object'])
    else:
        pass
