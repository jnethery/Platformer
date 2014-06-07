import engine.config as config
from engine.objectManager import objects
__author__ = 'josiah'

objectSet = {
    'level':[],
    'player':[],
    'enemies':[]
}

def initializeObjects():
    for object in objectSet['level']:
        object.setColor([120,120,120])

screen_height = config.gfx['screen']['screen_height']
screen_width = config.gfx['screen']['screen_width']

def cullObjects(objectList):
    culledList = []
    for object in objectList:
        objectRect = object.getRect()
        if objectRect.x < screen_width and objectRect.x + objectRect.w >= 0 and \
            objectRect.y < screen_height and objectRect.y + objectRect.h >= 0:
                culledList.append(object)
    return culledList

def getObjects():
    objectsList = []
    for objectKey in objectSet:
        for object in objectSet[objectKey]:
            objectsList.append(object)
    return objectsList

def getPhysicsObjects():
    objectsList = []
    for objectKey in objectSet:
        for object in objectSet[objectKey]:
            if type(object) is objects.PhysicsObject:
                objectsList.append(object)
    return objectsList

def getLevelObjects():
    objectsList = []
    for object in objectSet['level']:
        objectsList.append(object)
    return objectsList

def getPlayer():
    return objectSet['player'][0]