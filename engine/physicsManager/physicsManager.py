__author__ = 'josiah'
import pygame
import operator
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

        # test collisions on bottom
        if testVector[1] > 0:
            origin = [object.getRect().left, object.getRect().bottom]
            offset = [object.getRect().w, 0]
            if getTestVector(origin, destination, offset).colliderect(collisionSurface.getRect()):
                setPostCollisionPosition(object, collisionSurface)

        # test collisions on top
        if testVector[1] < 0:
            origin = [object.getRect().left, object.getRect().top]
            offset = [object.getRect().w, 0]
            if getTestVector(origin, destination, offset).colliderect(collisionSurface.getRect()):
                setPostCollisionPosition(object, collisionSurface)

        #test collisions on right
        if testVector[0] > 0:
            origin = [object.getRect().right, object.getRect().top]
            offset = [0, object.getRect().h]
            if getTestVector(origin, destination, offset).colliderect(collisionSurface.getRect()):
                setPostCollisionPosition(object, collisionSurface)

        #test collisions on left
        if testVector[0] < 0:
            origin = [object.getRect().left, object.getRect().top]
            offset = [0, object.getRect().h]
            if getTestVector(origin, destination, offset).colliderect(collisionSurface.getRect()):
                setPostCollisionPosition(object, collisionSurface)

def getTestVector(origin, destination, offset):
    return pygame.Rect(origin[0], origin[1],
                                 destination[0] - origin[0] + offset[0], destination[1] - origin[1] + offset[1])

def setPostCollisionPosition(object, collisionSurface):
    if type(object) is objects.PhysicsObject:

        vel = object.getVelocity()
        x_vel = vel[0]
        y_vel = vel[1]

        # testing top and bottom collisions
        if object.getRect().right > collisionSurface.getRect().left and \
                        object.getRect().left < collisionSurface.getRect().right:
            if object.getRect().top <= collisionSurface.getRect().top:
                object.getRect().bottom = collisionSurface.getRect().top
                y_vel = 0
            if object.getRect().bottom >= collisionSurface.getRect().bottom:
                object.getRect().top = collisionSurface.getRect().bottom
                y_vel = 0

        # testing left and right collisions
        if object.getRect().bottom > collisionSurface.getRect().top and \
                        object.getRect().top < collisionSurface.getRect().bottom:
            if object.getRect().left < collisionSurface.getRect().left:
                object.getRect().right = collisionSurface.getRect().left
                x_vel = 0
            if object.getRect().right > collisionSurface.getRect().right:
                object.getRect().left = collisionSurface.getRect().right
                x_vel = 0

        object.setVelocity([x_vel, y_vel])






