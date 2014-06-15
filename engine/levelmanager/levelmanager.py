__author__ = 'josiah'
import os
import sys
import pygame
import engine.config as config
from engine.objectmanager import objectmanager, objectclasses

current_level = None

object_codes = {
    'space':0,
    'level':1,
    'environment':2,
    'player':3,
    'enemies':4,
}

def set_level_data_path():
    os.chdir(os.path.join(os.getcwd(), 'data'))
    os.chdir(os.path.join(os.getcwd(), 'levels'))

def set_img_data_path():
    os.chdir(os.path.join(os.getcwd(), 'data'))
    os.chdir(os.path.join(os.getcwd(), 'img'))

def reset_path():
    os.chdir('..')
    os.chdir('..')

def get_cur_level():
    return current_level

def save_editor_level():
    tile_size = config.gfx['tile']['tile_size']
    min_x = sys.maxint
    min_y = sys.maxint
    max_x = 0
    max_y = 0
    objects = objectmanager.get_all_objects()
    for object in objects:
        object_rect = object.get_rect()
        if object_rect.x < min_x:
            min_x = object_rect.x
        if object_rect.x > max_x:
            max_x = object_rect.x
        if object_rect.y > max_y:
            max_y = object_rect.y
        if object_rect.y < min_y:
            min_y = object_rect.y
    rows = ((max_x - min_x)/tile_size + 1)
    columns = (max_y - min_y)/tile_size + 1

    object_array = []
    for j in range(0, columns, 1):
        object_array.append([])
        for i in range(0, rows, 1):
            object_array[j].append(str(object_codes['space']))
    for object_key in objectmanager.object_sets:
        for object in objectmanager.object_sets[object_key]:
            object_rect = object.get_rect()
            i = (object_rect.y - min_y)/tile_size
            j = (object_rect.x - min_x)/tile_size
            object_array[i][j] = str(object_codes[object_key])
    set_level_data_path()
    data = open(current_level, 'w')
    for object_row in object_array:
        data.write(' '.join(object_row))
        data.write('\n')
    data.close()
    print '...level saved'
    reset_path()

def load_level(level):
    global current_level
    current_level = level
    set_level_data_path()
    data = open(level, 'r')
    lines = data.readlines()
    data.close()
    reset_path()

    tile_size = config.gfx['tile']['tile_size']
    for i in range(0, len(lines), 1):
        object_list = lines[i].split(' ')
        for j in range(0, len(object_list), 1):
            origin = [tile_size*j, tile_size*i]
            size = [tile_size, tile_size]
            create_object(object_list[j], origin, size)
    if len(objectmanager.object_sets['player']) is 0:
        print 'Player object not set!'
        sys.exit()
    objectmanager.init_objects()

def create_object(object, origin, size):
    if object[0] is '1':
        objectmanager.object_sets['level'].append(objectclasses.Object(origin[0], origin[1], size[0], size[1]))
    if object[0] is '2':
        objectmanager.object_sets['environment'].append(objectclasses.Object(origin[0], origin[1], size[0], size[1]))
    if object[0] is '3':
        player_object = objectclasses.Entity(origin[0], origin[1], size[0], size[1])
        set_img_data_path()
        player_object.set_image(pygame.image.load('test.png'))
        reset_path()
        objectmanager.object_sets['player'].append(player_object)
    if object[0] is '4':
        objectmanager.object_sets['enemies'].append(objectclasses.Entity(origin[0], origin[1], size[0], size[1]))