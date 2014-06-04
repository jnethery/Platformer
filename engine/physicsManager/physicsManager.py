__author__ = 'josiah'
import pygame
from engine import config
from engine.processManager import process

def getPhysicsProcessQueue():
    physicsProcessQueue = []
    return physicsProcessQueue

def getMovement(object, vector):
    object.displace(vector)