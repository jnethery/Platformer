__author__ = 'josiah'
import pygame
from engine import config
from engine.processManager import process
from engine.objectManager import objectManager

def getPhysicsProcessQueue():
    physicsProcessQueue = []
    physicsProcessQueue += applyGravity()
    return physicsProcessQueue

def move(object, vector):
    object.displace(vector)

def applyGravity():
    processList = []
    objects = objectManager.getPhysicsObjects()
    for object in objects:
        object.applyGravity()
        params = {}
        params['object'] = object
        params['vector'] = object.getVelocityDisplacementVector()
        processList.append(process.getProcess('physics', 'move', params))
    return processList


