import engine.config as config
from engine.objectmanager import objectclasses
__author__ = 'josiah'

screen_height = config.gfx['screen']['screen_height']
screen_width = config.gfx['screen']['screen_width']

physics_object_sets = ['player', 'enemies']
interaction_object_sets = physics_object_sets + ['level']
entity_sets = physics_object_sets

object_sets = {
    'level':[],
    'environment':[],
    'player':[],
    'enemies':[],
}

physics_objects = None

font_objects_sets = {
    'fonts':[],
}

editor_object_sets = {
    'editor_menu':[],
    'editor_cursor':[],
}

def is_physics_object(object):
    return object.is_phys

def is_entity(object):
    return object.is_ent

def init_objects():
    for object in object_sets['level']:
        object.set_color([120,120,120])
    for object in object_sets['environment']:
        object.set_color([120,120,120])

def cull_append(list, object):
    if cull(object) is not None:
        list.append(object)

def cull(object):
    object_rect = object.get_rect()
    if object_rect.x < screen_width and object_rect.x + object_rect.w >= 0 and \
        object_rect.y < screen_height and object_rect.y + object_rect.h >= 0:
        return object
    return None

def get_all_objects():
    objects_list = []
    for object_key in object_sets:
        for object in object_sets[object_key]:
            objects_list.append(object)
    return objects_list

def get_objects():
    objects_list = []
    for object_key in object_sets:
        for object in object_sets[object_key]:
            cull_append(objects_list, object)
    return objects_list

def get_interaction_objects():
    objects_list = []
    for object_key in interaction_object_sets:
        for object in object_sets[object_key]:
            cull_append(objects_list, object)
    return objects_list

def get_editor_objects():
    objects_list = []
    for object_key in editor_object_sets:
        for object in editor_object_sets[object_key]:
            objects_list.append(object)
    return objects_list

def get_entity_objects():
    objects_list = []
    physics_objects = get_physics_objects()
    for object in physics_objects:
        if is_entity(object):
            cull_append(objects_list, object)
    return objects_list

def get_level_objects():
    objects_list = []
    for object in object_sets['level']:
        cull_append(objects_list, object)
    return objects_list

def get_font_objects():
    objects_list = []
    for object in font_objects_sets['fonts']:
        cull_append(objects_list, object)
    return objects_list

def get_physics_objects():
    return physics_objects

def set_physics_objects():
    objects_list = []
    for object_key in physics_object_sets:
        for object in object_sets[object_key]:
            cull_append(objects_list, object)
    global physics_objects
    physics_objects = objects_list

def killObjects():
    for entity_set in entity_sets:
        for object in object_sets[entity_set]:
            if not object.is_alive():
                object_sets[entity_set].remove(object)

def get_player():
    try:
        player = object_sets['player'][0]
    except:
        player = None
    return player