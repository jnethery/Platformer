import engine.config as config
from engine.objectManager import objects
__author__ = 'josiah'

physicsObjectSets = ['player', 'enemies']
interactionObjectSets = physicsObjectSets + ['level']
entitySets = physicsObjectSets

objectSet = {
    'level':[],
    'environment':[],
    'player':[],
    'enemies':[],
}

physicsObjects = None

fontObjectSet = {
    'fonts':[],
}

editorObjectSet = {
    'editorCursor':[],
}

def isPhysicsObject(object):
    return object.isPhysicsObject

def isEntity(object):
    return issubclass(object.__class__, objects.Entity)

def initializeObjects():
    for object in objectSet['level']:
        object.setColor([120,120,120])
    for object in objectSet['environment']:
        object.setColor([120,120,120])

screen_height = config.gfx['screen']['screen_height']
screen_width = config.gfx['screen']['screen_width']

def append(list, object):
    if cullObject(object) is not None:
        list.append(object)

def cullObject(object):
    objectRect = object.getRect()
    if objectRect.x < screen_width and objectRect.x + objectRect.w >= 0 and \
        objectRect.y < screen_height and objectRect.y + objectRect.h >= 0:
        return object
    return None

def getAllObjects():
    objectsList = []
    for objectKey in objectSet:
        for object in objectSet[objectKey]:
            objectsList.append(object)
    return objectsList

def getObjects():
    objectsList = []
    for objectKey in objectSet:
        for object in objectSet[objectKey]:
            append(objectsList, object)
    return objectsList

def getInteractionObjects():
    objectsList = []
    for objectKey in interactionObjectSets:
        for object in objectSet[objectKey]:
            append(objectsList, object)
    return objectsList

def getEditorObjects():
    objectsList = []
    for objectKey in editorObjectSet:
        for object in editorObjectSet[objectKey]:
            append(objectsList, object)
    return objectsList

def getPhysicsObjects():
    return physicsObjects

def setPhysicsObjects():
    objectsList = []
    for objectKey in physicsObjectSets:
        for object in objectSet[objectKey]:
            append(objectsList, object)
    global physicsObjects
    physicsObjects = objectsList

def getEntityObjects():
    objectsList = []
    physicsObjects = getPhysicsObjects()
    for object in physicsObjects:
        if isEntity(object):
            append(objectsList, object)
    return objectsList

def killObjects():
    for entitySet in entitySets:
        for object in objectSet[entitySet]:
            if not object.isAlive():
                objectSet[entitySet].remove(object)

def getLevelObjects():
    objectsList = []
    for object in objectSet['level']:
        append(objectsList, object)
    return objectsList

def getFontObjects():
    objectsList = []
    for object in fontObjectSet['fonts']:
        append(objectsList, object)
    return objectsList

def getPlayer():
    try:
        player = objectSet['player'][0]
    except:
        player = None
    return player