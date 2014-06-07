__author__ = 'josiah'
import pygame
from engine import config
from engine.processManager import process
from engine.objectManager import objectManager

screen_width = config.gfx['screen']['screen_width']
screen_height = config.gfx['screen']['screen_height']
screen_size = [screen_width, screen_height]
screen = pygame.display.set_mode(screen_size)

screen_scroll_trigger = [200, 100]
screen_scroll_speed = [4, 4]

RGB = [100, 100, 255]
RGB_DIR = [1,1,1]

def getGraphicsProcessQueue():
    graphicsProcessQueue = []
    graphicsProcessQueue.append(process.getProcess('gfx', 'fill', None))
    checkForCameraMotion()
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

def checkForCameraMotion():
    player = objectManager.getPlayer()

    if (player.getRect().right > screen_width - screen_scroll_trigger[0]):
        moveScreen([-screen_scroll_speed[0], 0])
    if (player.getRect().left < screen_scroll_trigger[0]):
        moveScreen([screen_scroll_speed[0], 0])

    if (player.getRect().bottom > screen_height - screen_scroll_trigger[1]):
        moveScreen([0, -screen_scroll_speed[1]])
    if (player.getRect().top < screen_scroll_trigger[1]):
        moveScreen([0, screen_scroll_speed[1]])

def moveScreen(vector):
    objects = objectManager.getObjects()
    for object in objects:
        object.displace(vector)