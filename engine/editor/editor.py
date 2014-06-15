__author__ = 'josiah'
import engine.config as config
from engine.objectmanager import objectmanager, objectclasses
from engine.levelmanager import levelmanager
from engine.gfxmanager import gfxmanager

tile_size = config.gfx['tile']['tile_size']
screen_width = config.gfx['screen']['screen_width']
screen_height = config.gfx['screen']['screen_height']
menu_width = config.editor['menu_width']

def save_editor_level():
    levelmanager.save_editor_level()

def show_editor_cursor(mouse_pos):
    pos_x = (mouse_pos[0] % (screen_width + menu_width)/tile_size)*tile_size
    pos_y = (mouse_pos[1] % screen_height/tile_size)*tile_size
    pos_x, pos_y = add_offset(pos_x, pos_y)
    if pos_x < screen_width:
        if len(objectmanager.editor_object_sets['editor_cursor']) == 0:
            objectmanager.editor_object_sets['editor_cursor'].append(objectclasses.Object(pos_x, pos_y, tile_size, tile_size))
        else:
            objectmanager.editor_object_sets['editor_cursor'][0].set_pos([pos_x, pos_y])

def add_offset(pos_x, pos_y):
    screen_offset = gfxmanager.get_screen_offset()
    pos_x = pos_x - (pos_x - screen_offset[0])%tile_size
    pos_y = pos_y - (pos_y - screen_offset[1])%tile_size
    return pos_x, pos_y

def add_object(mouse_pos):
    if mouse_pos[0] < screen_width - tile_size:
        pos_x = (mouse_pos[0] % screen_width/tile_size)*tile_size
        pos_y = (mouse_pos[1] % screen_height/tile_size)*tile_size
        pos_x, pos_y = add_offset(pos_x, pos_y)
        object = objectclasses.Object(pos_x, pos_y, tile_size, tile_size)
        object.set_color([0,0,0])
        objectmanager.object_sets['level'].append(object)

def delete_object(mouse_pos):
    if mouse_pos[0] < screen_width - tile_size:
        pos_x = (mouse_pos[0] % screen_width/tile_size)*tile_size
        pos_y = (mouse_pos[1] % screen_height/tile_size)*tile_size
        pos_x, pos_y = add_offset(pos_x, pos_y)
        object_data = get_object_at_coord(pos_x, pos_y)
        if object_data is not None:
            object = object_data['object']
            type = object_data['type']
            objectmanager.object_sets[type].remove(object)

def get_object_at_coord(pos_x, pos_y):
    for object_key in objectmanager.object_sets:
        for object in objectmanager.object_sets[object_key]:
            object_rect = object.get_rect()
            if object_rect.x == pos_x and object_rect.y == pos_y:
                return {'object':object, 'type':object_key}
    return None