__author__ = 'josiah'
import os
import sys
import pygame
import engine.config as config
import string
from engine.objectmanager import objectmanager, objectclasses

current_level = None

def set_level_data_path():
    os.chdir(os.path.join(os.getcwd(), 'data'))
    os.chdir(os.path.join(os.getcwd(), 'levels'))

def set_object_data_path():
    os.chdir(os.path.join(os.getcwd(), 'data'))
    os.chdir(os.path.join(os.getcwd(), 'object_data'))

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
            object_array[j].append('FFFF')
    for object_key in objectmanager.object_sets:
        for object in objectmanager.object_sets[object_key]:
            object_rect = object.get_rect()
            i = (object_rect.y - min_y)/tile_size
            j = (object_rect.x - min_x)/tile_size
            object_array[i][j] = '%04X' % object.index
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
    object_data = get_object_data(level)
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
            create_object(object_list[j], origin, size, object_data)
    if len(objectmanager.object_sets['player']) == 0:
        print 'Player object not set!'
        sys.exit()

def create_object(object, origin, size, object_data):
    object_index = int(object, 16)
    if object_index != int('FFFF', 16):
        object_data = object_data[object_index]
        object_data = object_data.split(' ')
        object_class = getattr(objectclasses, object_data[0])
        object_set = object_data[1]
        num_fields = int(object_data[2])
        object = object_class(origin[0], origin[1], size[0], size[1], object_index)
        for i in range(0, num_fields, 2):
            setattr(object, object_data[3 + i], parse_variable(object_data[4 + i]))
        objectmanager.object_sets[object_set].append(object)

def get_object_data(level):
    object_data_list = []
    set_object_data_path()
    index = int(string.split(level, '_')[-1])
    object_index = open('object_index', 'r')
    object_index_lines = object_index.readlines()
    object_index.close()
    object_data = open('object_data', 'r')
    object_data_lines = object_data.readlines()
    object_data.close()
    object_indices = object_index_lines[index]
    object_indices = object_indices.split(',')
    for i in range(0, len(object_indices), 1):
        object_data_list.append(object_data_lines[int(object_indices[i])])
    reset_path()
    return object_data_list

def parse_variable(variable):
    variable = variable.replace('\n', '')
    if variable[0] == '[':
        list = variable.replace('[', '')
        list = list.replace(']', '')
        list = list.split(',')
        list = [int(elem) for elem in list]
        return list
    elif variable[0] == "'":
        set_img_data_path()
        img = pygame.image.load(variable.replace("'", ''))
        reset_path()
        return img
    else:
        return int(variable)

