from engine.objectManager import objects
__author__ = 'josiah'

objectSet = {
    'level':[
        objects.Object(0,380,200,100),
        objects.Object(200,380,100,100),
        objects.Object(400,380,100,100),
        objects.Object(500,280,100,200),
        objects.Object(200,350,35,35),
        objects.Object(200,275,35,35),
        objects.Object(0,0,10,512),
    ],
    'player':[objects.PhysicsObject(40,0,20,20)],
    'enemies':[
        #objects.PhysicsObject(100,0,10,10),
        #objects.PhysicsObject(200,0,10,10),
    ],
}

for object in objectSet['level']:
    object.setColor([120,120,120])

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