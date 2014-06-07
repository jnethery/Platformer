__author__ = 'josiah'
import sys
from engine.eventManager import eventManager
from engine.graphicsManager import graphicsManager
from engine.physicsManager import physicsManager
from engine.objectManager import objectManager

def getProcessQueue():
    processQueue = []
    physicsManager.processPhysics()
    processQueue += eventManager.getEventProcessQueue()
    processQueue += graphicsManager.getGraphicsProcessQueue()
    return processQueue

def runProcessQueue():
    processQueue = getProcessQueue()
    for process in processQueue:
        system = process['system']
        method = process['method']
        params = process['params']
        if system is 'sys':
            runSystemProcess(method, params)
        if system is 'physics':
            runPhysicsProcess(method, params)
        if system is 'gfx':
            runGraphicsProcess(method, params)
        if system is 'sound':
            pass
        else:
            pass

def runSystemProcess(method, params):
    if method is 'exit':
        sys.exit()
    else:
        pass

def runPhysicsProcess(method, params):
    if method is 'applyVelocity':
        object = params['object']
        vector = params['vector']
        physicsManager.applyVelocity(object, vector)
    if method is 'jump':
        object = params['object']
        physicsManager.jump(object)

def runGraphicsProcess(method, params):
    if method is 'fill':
        graphicsManager.fillScreen()
    if method is 'flip':
        graphicsManager.flipScreen()
    if method is 'blit':
        graphicsManager.blit(params['object'])
    else:
        pass
