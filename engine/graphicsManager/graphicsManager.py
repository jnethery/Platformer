__author__ = 'josiah'
import pygame
from engine import config
from engine.processManager import process
from engine.objectManager import objectManager

screen_width = config.gfx['screen']['screen_width']
screen_height = config.gfx['screen']['screen_height']
screen_size = [screen_width, screen_height]
screen = pygame.display.set_mode(screen_size)
RGB = [100, 100, 255]
RGB_DIR = [1,1,1]

def getGraphicsProcessQueue():
    graphicsProcessQueue = []
    graphicsProcessQueue.append(process.getProcess('gfx', 'fill', None))
    graphicsProcessQueue += blitObjects()
    graphicsProcessQueue.append(process.getProcess('gfx', 'flip', None))
    return graphicsProcessQueue

def fillScreen():
    if RGB_DIR[0] is 1:
        if RGB[0] < 255 - 1:
            RGB[0] += 2
        else:
            RGB_DIR[0] = 0
    else:
        if RGB[0] > 0 + 1:
            RGB[0] -= 2
        else:
            RGB_DIR[0] = 1
    screen.fill(RGB)

def flipScreen():
    pygame.display.flip()

def blit(object):
    pygame.draw.rect(screen, object.getColor(), object.getRect())

def blitObjects():
    processList = []
    objects = objectManager.getObjects()
    for object in objects:
        params = {}
        params['object'] = object
        processList.append(process.getProcess('gfx', 'blit', params))
    return processList