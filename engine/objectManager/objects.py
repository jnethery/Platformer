__author__ = 'josiah'
import pygame
import operator
from engine import config
from engine.systemManager import clock

class Object(object):

    def __init__(self, x, y, w, h):
        self.Rect = pygame.Rect(x, y, w, h)
        self.color = [255,255,255]

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def getPosition(self):
        return [self.Rect.x, self.Rect.y]

    def getRect(self):
        return self.Rect

    def setPosition(self, vector):
        [self.Rect.x, self.Rect.y] = vector

    def displace(self, vector):
        self.Rect = self.Rect.move(vector[0], vector[1])

class PhysicsObject(Object):

    def __init__(self, x, y, w, h):
        super(self.__class__, self).__init__(x, y, w, h)
        self.gravity = 10
        self.pixels_per_meter = 10

        self.velocity = [0, 0]
        self.run_velocity = 30
        self.jump_velocity = 30
        self.damping = self.run_velocity/2
        self.max_velocity = [self.run_velocity, 100]

        self.mass = 1

    def applyPhysics(self):
        self.applyGravity()
        self.applyDisplacement()
        self.applyDamping()

    def applyVelocity(self, vector):
        self.velocity = map(operator.add, self.velocity, vector)
        for i in range(0, len(self.velocity), 1):
            if self.velocity[i] > self.max_velocity[i]:
                self.velocity[i] = self.max_velocity[i]
            elif self.velocity[i] < -self.max_velocity[i]:
                self.velocity[i] = -self.max_velocity[i]

    def applyGravity(self):
        self.applyVelocity([0, (self.gravity*self.pixels_per_meter)/clock.get_fps()])

    def applyDisplacement(self):
        self.displace(self.getVelocityDisplacementVector())

    def applyDamping(self):
        damping = (self.damping*self.pixels_per_meter)/clock.get_fps()
        if self.velocity[0] > damping:
           self.velocity[0] -= damping
        elif self.velocity[0] < -damping:
           self.velocity[0] += damping

    def getVelocityDisplacementVector(self):
        return [(vel*self.pixels_per_meter)/clock.get_fps() for vel in self.velocity]

    def getVelocity(self):
        return self.velocity

    def setVelocity(self, vector):
        self.velocity = vector

    def getMass(self):
        return self.mass

    def setMass(self, mass):
        self.mass = mass