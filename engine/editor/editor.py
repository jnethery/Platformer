__author__ = 'josiah'
import engine.config as config
from engine.objectManager import objectManager, objects
from engine.processManager import process
from engine.levelManager import levelManager

tile_size = config.gfx['tile']['tile_size']
screen_width = config.gfx['screen']['screen_width']
screen_height = config.gfx['screen']['screen_height']

def saveLevel():
    levelManager.saveEditorLevel()

def addObject(mousePosition):
    params = {}
    pos_x = (mousePosition[0] % screen_width/tile_size)*tile_size
    pos_y = (mousePosition[1] % screen_height/tile_size)*tile_size
    params['object'] = objects.Object(pos_x, pos_y, tile_size, tile_size)
    params['object'].setColor([0,0,0])
    return process.getProcess('editor', 'addObject', params)

def deleteObject(mousePosition):
    params = {}
    pos_x = (mousePosition[0] % screen_width/tile_size)*tile_size
    pos_y = (mousePosition[1] % screen_height/tile_size)*tile_size
    object = getObjectAtPosition(pos_x, pos_y)
    params['object'] = object['object']
    params['type'] = object['type']
    return process.getProcess('editor', 'deleteObject', params)

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