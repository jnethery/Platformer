from engine.objectManager import objects
__author__ = 'josiah'

objectSet = {
    'level':[
        objects.Object(0,400,512,50)
    ],
    'player':[objects.PhysicsObject(0,0,10,10)],
    'enemies':[
        objects.PhysicsObject(100,0,10,10),
        objects.PhysicsObject(200,0,10,10),
        objects.PhysicsObject(300,0,10,10),
    ],
}

objectSet['level'][0].setColor([0,0,0])

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