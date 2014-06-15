__author__ = 'josiah'
import pygame
import operator
from engine import config
from engine.systemManager import clock
from engine.triggerManager import trigger

class Object(object):

    def __init__(self, x, y, w, h):
        self.Rect = pygame.Rect(x, y, w, h)
        self.color = [255,255,255]
        self.image = None

        self.isPhysicsObject = False
        self.isEntity = False

    def setImage(self, image):
        self.image = image

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

class FontObject(Object):

    def __init__(self, x, y, w, h):
        super(FontObject, self).__init__(x, y, w, h)
        self.font = pygame.font.Font(pygame.font.match_font('Arial'), 12)
        self.message = 'None'
        self.text = self.font.render(self.message, 1, self.color)

    def setMessage(self, message):
        self.message = message

class PhysicsObject(Object):

    def __init__(self, x, y, w, h):
        super(PhysicsObject, self).__init__(x, y, w, h)
        self.gravity = 10
        self.pixels_per_meter = 10
        self.velocity = [0, 0]
        self.run_velocity = 30
        self.jump_velocity = 40
        self.damping = self.run_velocity/2
        self.max_velocity = [self.run_velocity, 100]
        self.mass = 1

        self.isPhysicsObject = True

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

class Entity(PhysicsObject):

    def __init__(self, x, y, w, h):
        super(Entity, self).__init__(x, y, w, h)
        self.health = 100

        self.isPhysicsObject = True

    def applyDamage(self, damage):
        self.health -= damage

    def isAlive(self):
        return self.health > 0