__author__ = 'josiah'
import sys
from engine.eventManager import eventManager
from engine.graphicsManager import graphicsManager
from engine.physicsManager import physicsManager
from engine.objectManager import objectManager
from engine.editor import editor

def getEditorProcessQueue():
    processQueue = []
    processQueue += eventManager.getEditorEventProcessQueue()
    processQueue += graphicsManager.getEditorGraphicsProcessQueue()
    return processQueue

def getProcessQueue():
    processQueue = []
    objectManager.setPhysicsObjects()
    physicsManager.processPhysics()
    objectManager.killObjects()
    processQueue += eventManager.getEventProcessQueue()
    processQueue += graphicsManager.getGraphicsProcessQueue()
    return processQueue

def runProcessQueue(engineState):
    if engineState is 0:
        processQueue = getProcessQueue()
    if engineState is 1:
        processQueue = getEditorProcessQueue()
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
        if system is 'editor':
            runEditorProcess(method, params)
        else:
            pass

def runEditorProcess(method, params):
    if method is 'save':
        editor.saveLevel()
    if method is 'addObject':
        object = params['object']
        objectManager.objectSet['level'].append(object)
    if method is 'deleteObject':
        object = params['object']
        type = params['type']
        if type is not None:
            objectManager.objectSet[type].remove(object)

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
    if method is 'moveScreen':
        graphicsManager.moveScreen(params['vector'])
    if method is 'fill':
        graphicsManager.fillScreen()
    if method is 'flip':
        graphicsManager.flipScreen()
    if method is 'blit':
        graphicsManager.blit(params['object'])
    else:
        pass
