__author__ = 'josiah'
import pygame
import operator
from engine import config
from engine.processManager import process
from engine.objectManager import objectManager, objects

def processPhysics():
    processCollisions()
    applyPhysics()

def applyVelocity(object, vector):
    object.applyVelocity(vector)

def jump(object):
    vel = object.getVelocity()
    object.setVelocity([vel[0], -object.jump_velocity])

def applyPhysics():
    objects = objectManager.getPhysicsObjects()
    for object in objects:
        object.applyPhysics()

def processCollisions():
    objects = objectManager.getObjects()
    for i in range(0, len(objects), 1):
        for j in range(i+1, len(objects), 1):
            processCollision(objects[i], objects[j])

def processCollision(object, collisionSurface):
    if type(object) is not objects.PhysicsObject and type(collisionSurface) is not objects.PhysicsObject:
        pass
    elif type(object) is not objects.PhysicsObject:
        processCollision(collisionSurface, object)
    else:
        origin = object.getPosition()
        destination = map(operator.add, origin, object.getVelocityDisplacementVector())
        testVector = [destination[0] - origin[0], destination[1] - origin[1]]
        offset = [0,0]

        if testVector[1] > 0:
            origin = [object.getRect().left, object.getRect().bottom]
            offset[0] = object.getRect().w
        testVector = pygame.Rect(origin[0], origin[1],
                                 destination[0] - origin[0] + offset[0], destination[1] - origin[1] + offset[1])
        if testVector.colliderect(collisionSurface.getRect()):
            setPostCollisionPosition(object, collisionSurface)

def isGrounded(object):
    objects = objectManager.getObjects()
    if (object.getRect().collidelist(objects)):
        pass

def setPostCollisionPosition(object, collisionSurface):
    if type(object) is objects.PhysicsObject:
        if object.getRect().top <= collisionSurface.getRect().top:
            object.getRect().bottom = collisionSurface.getRect().top
            vel = object.getVelocity()
            x_vel = vel[0]
            y_vel = 0
            object.setVelocity([x_vel, y_vel])






