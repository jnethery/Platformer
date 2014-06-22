__author__ = 'josiah'
import pygame
import operator
from engine.sysmanager import clock
from engine.physicsmanager import physicsmanager

class Object(object):

    def __init__(self, x, y, w, h, idx = None):
        self.index = idx
        self.Rect = pygame.Rect(x, y, w, h)
        self.color = [255,255,255]
        self.image = None
        self.is_phys = False
        self.is_ent = False

    def set_image(self, image):
        self.image = image

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def get_pos(self):
        return [self.Rect.x, self.Rect.y]

    def set_pos(self, vector):
        [self.Rect.x, self.Rect.y] = vector

    def get_rect(self):
        return self.Rect

    def move_rect(self, vector):
        self.Rect = self.Rect.move(vector[0], vector[1])

class FontObject(Object):

    def __init__(self, x, y, w, h, idx):
        super(FontObject, self).__init__(x, y, w, h, idx)
        self.font = pygame.font.Font(pygame.font.match_font('Arial'), 12)
        self.msg = 'None'
        self.text = self.font.render(self.msg, 1, self.color)

    def set_msg(self, msg):
        self.msg = msg

class PhysicsObject(Object):

    def __init__(self, x, y, w, h, idx):
        super(PhysicsObject, self).__init__(x, y, w, h, idx)
        self.gravity = 10
        self.pixels_per_meter = 12
        self.velocity = [0, 0]
        self.run_velocity = 30
        self.jump_velocity = 40
        self.damping = self.run_velocity/1
        self.max_velocity = [self.run_velocity, 100]
        self.mass = 1
        self.is_phys = True

    def apply_physics(self):
        self.apply_gravity()
        self.apply_disp()
        self.apply_damp()

    def apply_vel(self, vector):
        self.velocity = map(operator.add, self.velocity, vector)
        for i in range(0, len(self.velocity), 1):
            if self.velocity[i] > self.max_velocity[i]:
                self.velocity[i] = self.max_velocity[i]
            elif self.velocity[i] < -self.max_velocity[i]:
                self.velocity[i] = -self.max_velocity[i]

    def apply_gravity(self):
        self.apply_vel([0, (self.gravity*self.pixels_per_meter)/clock.get_fps()])

    def apply_disp(self):
        self.move_rect(self.get_motion_vector())

    def apply_damp(self):
        damping = (self.damping*self.pixels_per_meter)/clock.get_fps()
        if self.velocity[0] > damping:
           self.velocity[0] -= damping
        elif self.velocity[0] < -damping:
           self.velocity[0] += damping

    def get_motion_vector(self):
        return [(vel*self.pixels_per_meter)/clock.get_fps() for vel in self.velocity]

    def get_vel(self):
        return self.velocity

    def set_vel(self, vector):
        self.velocity = vector

    def get_mass(self):
        return self.mass

    def set_mass(self, mass):
        self.mass = mass

class Entity(PhysicsObject):

    def __init__(self, x, y, w, h, idx):
        super(Entity, self).__init__(x, y, w, h, idx)
        self.health = 100
        self.is_phys = True

    def apply_damage(self, damage):
        self.health -= damage

    def is_alive(self):
        return self.health > 0

    def jump(self):
        self.apply_vel([self.velocity[0], -self.jump_velocity])

class Player(Entity):

    def __init__(self, x, y, w, h, idx):
        super(Player, self).__init__(x, y, w, h, idx)

    def apply_vel(self, vector):
        is_grounded = physicsmanager.is_grounded(self)
        if not is_grounded:
            vector[0] = 0.5*vector[0]
        self.velocity = map(operator.add, self.velocity, vector)
        for i in range(0, len(self.velocity), 1):
            if self.velocity[i] > self.max_velocity[i]:
                self.velocity[i] = self.max_velocity[i]
            elif self.velocity[i] < -self.max_velocity[i]:
                self.velocity[i] = -self.max_velocity[i]

