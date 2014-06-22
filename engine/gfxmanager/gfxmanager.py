__author__ = 'josiah'
import pygame
import operator
from engine import config
from engine.objectmanager import objectmanager, classes

screen_width = config.gfx['screen']['screen_width']
screen_height = config.gfx['screen']['screen_height']
screen_size = [screen_width, screen_height]
editor_menu_width = config.editor['menu_width']

screen = None

screen_scroll_trigger = [screen_width/3, screen_height/6]
screen_scroll_speed = [4, 4]
screen_offset = [0, 0]

RGB = [100, 100, 255]
RGB_DIR = [1,1,1]

def init_screen(engine_state):
    global screen
    if engine_state == 0:
        screen = pygame.display.set_mode(screen_size)
    elif engine_state == 1:
        screen_size[0] += editor_menu_width
        screen = pygame.display.set_mode(screen_size)
        init_editor_objects()

def init_editor_objects():
    tile_size = config.gfx['tile']['tile_size']
    editor_menu = classes.Object(screen_width, 0, editor_menu_width, screen_height)
    editor_menu.set_color([20,20,20])
    objectmanager.editor_object_sets['editor_menu'].append(editor_menu)

def run_editor_gfx_processes():
    fill_screen()
    blit_objects()
    flip_screen()

def run_gfx_processes():
    fill_screen()
    get_camera_motion()
    blit_objects()
    flip_screen()

def fill_screen():
    if RGB_DIR[0] is 1:
        if RGB[0] < 255 - 1:
            RGB[0] += 2
        else:
            RGB_DIR[0] = 0
    else:
        if RGB[0] > 0 + 1:
            RGB[0] -= 2
        else:
            RGB_DIR[0] = 1
    screen.fill(RGB)

def flip_screen():
    pygame.display.flip()

def blit(object):
    if object.image is not None:
        screen.blit(object.image, object.get_rect())
    else:
        pygame.draw.rect(screen, object.get_color(), object.get_rect())


def blit_objects():
    objects = objectmanager.get_objects()
    objects += objectmanager.get_font_objects()
    objects += objectmanager.get_editor_objects()
    for object in objects:
        blit(object)

def get_camera_motion():
    player = objectmanager.get_player()
    camera_motion = False
    if player is not None:
        if (player.get_rect().right > screen_width - screen_scroll_trigger[0]):
            move_screen([-screen_scroll_speed[0], 0])
            camera_motion = True
        elif (player.get_rect().left < screen_scroll_trigger[0]):
            move_screen([screen_scroll_speed[0], 0])
            camera_motion = True

        if (player.get_rect().bottom > screen_height - screen_scroll_trigger[1]):
            move_screen([0, -screen_scroll_speed[1]])
            camera_motion = True
        elif (player.get_rect().top < screen_scroll_trigger[1]):
            move_screen([0, screen_scroll_speed[1]])
            camera_motion = True
    return camera_motion

def move_screen(vector):
    global screen_offset
    screen_offset = map(operator.add, screen_offset, vector)
    objects = objectmanager.get_all_objects()
    for object in objects:
        object.move_rect(vector)

def get_screen_offset():
    return screen_offset