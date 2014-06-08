__author__ = 'josiah'
import os, sys
import engine.config as config
from engine.objectManager import objectManager, objects

current_level = None

def setPath():
    os.chdir(os.path.join(os.getcwd(), 'levelManager'))
    os.chdir(os.path.join(os.getcwd(), 'data'))

def getCurrentLevel():
    return current_level

def saveEditorLevel():
    tile_size = config.gfx['tile']['tile_size']
    min_x = sys.maxint
    min_y = sys.maxint
    max_x = 0
    max_y = 0
    objects = objectManager.getObjects()
    for object in objects:
        objectRect = object.getRect()
        if objectRect.x < min_x:
            min_x = objectRect.x
        if objectRect.x > max_x:
            max_x = objectRect.x
        if objectRect.y > max_y:
            max_y = objectRect.y
        if objectRect.y < min_y:
            min_y = objectRect.y
    rows = ((max_x - min_x)/tile_size + 1)
    columns = (max_y - min_y)/tile_size + 1

    objectArray = []
    for j in range(0, columns, 1):
        objectArray.append([])
        for i in range(0, rows, 1):
            objectArray[j].append('00')
    for objectKey in objectManager.objectSet:
        for object in objectManager.objectSet[objectKey]:
            objectRect = object.getRect()
            i = (objectRect.y - min_y)/tile_size
            j = (objectRect.x - min_x)/tile_size
            if objectKey is 'level':
                objectArray[i][j] = '01'
            if objectKey is 'player':
                objectArray[i][j] = '10'
    setPath()
    data = open(current_level, 'w')
    for objectRow in objectArray:
        data.write(' '.join(objectRow))
        data.write('\n')
    data.close()
    print '...level saved'

def loadLevel(level):
    global current_level
    current_level = level
    setPath()
    data = open(level, 'r')
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