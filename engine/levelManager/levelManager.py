__author__ = 'josiah'
import os, sys
import pygame
import engine.config as config
from engine.objectManager import objectManager, objects

current_level = None

objectCodes = {
    'space':0,
    'level':1,
    'environment':2,
    'player':3,
    'enemies':4,
}

def setLevelDataPath():
    os.chdir(os.path.join(os.getcwd(), 'data'))
    os.chdir(os.path.join(os.getcwd(), 'levels'))

def setImageDataPath():
    os.chdir(os.path.join(os.getcwd(), 'data'))
    os.chdir(os.path.join(os.getcwd(), 'img'))

def resetPath():
    os.chdir('..')
    os.chdir('..')

def getCurrentLevel():
    return current_level

def saveEditorLevel():
    tile_size = config.gfx['tile']['tile_size']
    min_x = sys.maxint
    min_y = sys.maxint
    max_x = 0
    max_y = 0
    objects = objectManager.getAllObjects()
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
            objectArray[j].append(str(objectCodes['space']))
    for objectKey in objectManager.objectSet:
        for object in objectManager.objectSet[objectKey]:
            objectRect = object.getRect()
            i = (objectRect.y - min_y)/tile_size
            j = (objectRect.x - min_x)/tile_size
            objectArray[i][j] = str(objectCodes[objectKey])
    setLevelDataPath()
    data = open(current_level, 'w')
    for objectRow in objectArray:
        data.write(' '.join(objectRow))
        data.write('\n')
    data.close()
    print '...level saved'
    resetPath()

def loadLevel(level):
    global current_level
    current_level = level
    setLevelDataPath()
    data = open(level, 'r')
    lines = data.readlines()
    data.close()
    resetPath()

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
    if object[0] is '1':
        objectManager.objectSet['level'].append(objects.Object(origin[0], origin[1], size[0], size[1]))
    if object[0] is '2':
        objectManager.objectSet['environment'].append(objects.Object(origin[0], origin[1], size[0], size[1]))
    if object[0] is '3':
        playerObject = objects.Entity(origin[0], origin[1], size[0], size[1])
        setImageDataPath()
        playerObject.setImage(pygame.image.load('test.png'))
        resetPath()
        objectManager.objectSet['player'].append(playerObject)
    if object[0] is '4':
        objectManager.objectSet['enemies'].append(objects.Entity(origin[0], origin[1], size[0], size[1]))