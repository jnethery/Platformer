__author__ = 'josiah'
import os, sys
import engine.config as config
from engine.objectManager import objectManager, objects

def loadLevel(level):
    levelDataRoot = os.getcwd() + '/levelManager/data/'
    data = open(levelDataRoot + level, 'r')
    lines = data.readlines()
    data.close()

    tile_size = config.gfx['tile']['tile_size']
    for i in range(0, len(lines), 1):
        objectList = lines[i].split(' ')
        for j in range(0, len(objectList), 1):
            origin = [tile_size*j, tile_size*i]
            size = [tile_size, tile_size]
            createObject(objectList[j], origin, size)
    if len(objectManager.objectSet['player']) is 0:
        print 'Player object not set!'
        sys.exit()
    objectManager.initializeObjects()

def createObject(object, origin, size):
    if object[0] is '0':
        if object[1] is '1':
            objectManager.objectSet['level'].append(objects.Object(origin[0], origin[1], size[0], size[1]))
    if object[0] is '1':
        if object[1] is '0':
            objectManager.objectSet['player'].append(objects.PhysicsObject(origin[0], origin[1], size[0], size[1]))
        if object[1] is '1':
            objectManager.objectSet['enemies'].append(objects.PhysicsObject(origin[0], origin[1], size[0], size[1]))