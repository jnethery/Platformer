__author__ = 'josiah'

class Object:

    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def getPosition(self):
        return [self.x, self.y]

    def getRect(self):
        return [self.x, self.y, self.w, self.h]

    def setPosition(self, x, y):
        self.x = x
        self.y = y

    def displace(self, vector):
        self.x += vector[0]
        self.y += vector[1]
