__author__ = 'josiah'
import pygame
import engine.config as config
from engine.objectManager import objectManager, objects
from engine.processManager import process
from engine.levelManager import levelManager
from engine.graphicsManager import graphicsManager

tile_size = config.gfx['tile']['tile_size']
screen_width = config.gfx['screen']['screen_width']
screen_height = config.gfx['screen']['screen_height']
menu_width = config.editor['menu_width']

def saveLevel():
    levelManager.saveEditorLevel()

def showEditorCursor(mousePosition):
    pos_x = (mousePosition[0] % (screen_width + menu_width)/tile_size)*tile_size
    pos_y = (mousePosition[1] % screen_height/tile_size)*tile_size
    pos_x, pos_y = addOffset(pos_x, pos_y)
    if len(objectManager.editorObjectSet['editorCursor']) == 0:
        objectManager.editorObjectSet['editorCursor'].append(objects.Object(pos_x, pos_y, tile_size, tile_size))
    else:
        objectManager.editorObjectSet['editorCursor'][0].setPosition([pos_x, pos_y])

def addOffset(pos_x, pos_y):
    screen_offset = graphicsManager.getScreenOffset()
    pos_x = pos_x - (pos_x - screen_offset[0])%tile_size
    pos_y = pos_y - (pos_y - screen_offset[1])%tile_size
    return pos_x, pos_y

def addObject(mousePosition):
    if mousePosition[0] < screen_width - tile_size:
        params = {}
        pos_x = (mousePosition[0] % screen_width/tile_size)*tile_size
        pos_y = (mousePosition[1] % screen_height/tile_size)*tile_size
        pos_x, pos_y = addOffset(pos_x, pos_y)
        params['object'] = objects.Object(pos_x, pos_y, tile_size, tile_size)
        params['object'].setColor([0,0,0])
        return process.getProcess('editor', 'addObject', params)
    return process.getProcess(None, None, None)

def deleteObject(mousePosition):
    if mousePosition[0] < screen_width - tile_size:
        params = {}
        pos_x = (mousePosition[0] % screen_width/tile_size)*tile_size
        pos_y = (mousePosition[1] % screen_height/tile_size)*tile_size
        pos_x, pos_y = addOffset(pos_x, pos_y)
        object = getObjectAtPosition(pos_x, pos_y)
        params['object'] = object['object']
        params['type'] = object['type']
        return process.getProcess('editor', 'deleteObject', params)
    return process.getProcess(None, None, None)

def getObjectAtPosition(pos_x, pos_y):
    params = {}
    for objectKey in objectManager.objectSet:
        for object in objectManager.objectSet[objectKey]:
            objectRect = object.getRect()
            if objectRect.x == pos_x and objectRect.y == pos_y:
                params['object'] = object
                params['type'] = objectKey
                return params
    params['object'] = None
    params['type'] = None
    return params