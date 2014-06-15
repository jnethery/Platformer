__author__ = 'josiah'
import pygame
import operator
from engine.objectmanager import objectmanager

def is_physics_object(object):
    return objectmanager.physics_objects.__contains__(object)

def process_physics():
    process_collisions()
    apply_physics()

def apply_vel(object, vector):
    object.apply_vel(vector)

def jump(object):
    if is_grounded(object):
        vel = object.get_vel()
        object.set_vel([vel[0], -object.jump_velocity])

def apply_physics():
    objects = objectmanager.get_physics_objects()
    for object in objects:
        object.apply_physics()

def process_collisions():
    objects = objectmanager.get_interaction_objects()
    is_physics = [None]*len(objects)
    for i in range(0, len(objects), 1):
        if i == 0:
            is_physics[i] = is_physics_object(objects[i])
        for j in range(i+1, len(objects), 1):
            if i == 0:
                is_physics[j] = is_physics_object(objects[j])
            process_collision(objects[i], objects[j], is_physics[i], is_physics[j])
            process_collision(objects[j], objects[i], is_physics[j], is_physics[i])

def process_collision(object, coll_surface, object_is_physics, coll_surface_is_physics):
    if not object_is_physics and not coll_surface_is_physics:
        pass
    elif not object_is_physics:
        process_collision(coll_surface, object, coll_surface_is_physics, object_is_physics)
    else:
        origin = object.get_pos()
        destination = map(operator.add, origin, object.get_motion_vector())
        test_vector = [destination[0] - origin[0], destination[1] - origin[1]]

        # test collisions on bottom
        if test_vector[1] > 0:
            origin = [object.get_rect().left, object.get_rect().bottom]
            offset = [object.get_rect().w, 0]
            if get_test_vector_rect(origin, destination, offset).colliderect(coll_surface.get_rect()):
                set_post_collision_pos(object, coll_surface)

        # test collisions on top
        if test_vector[1] < 0:
            origin = [object.get_rect().left, object.get_rect().top + test_vector[1]]
            offset = [object.get_rect().w, 0]
            if get_test_vector_rect(origin, destination, offset).colliderect(coll_surface.get_rect()):
                set_post_collision_pos(object, coll_surface)

        #test collisions on right
        if test_vector[0] > 0:
            origin = [object.get_rect().right, object.get_rect().top]
            offset = [0, object.get_rect().h]
            if get_test_vector_rect(origin, destination, offset).colliderect(coll_surface.get_rect()):
                set_post_collision_pos(object, coll_surface)

        #test collisions on left
        if test_vector[0] < 0:
            origin = [object.get_rect().left + test_vector[0], object.get_rect().top]
            offset = [0, object.get_rect().h]
            if get_test_vector_rect(origin, destination, offset).colliderect(coll_surface.get_rect()):
                set_post_collision_pos(object, coll_surface)

def get_test_vector_rect(origin, destination, offset):
    return pygame.Rect(origin[0], origin[1],
        destination[0] - origin[0] + offset[0], destination[1] - origin[1] + offset[1])

def set_post_collision_pos(object, coll_surface):
    if is_physics_object(object):

        vel = object.get_vel()
        x_vel = vel[0]
        y_vel = vel[1]

        collision_offsets = [object.get_rect().w/4, object.get_rect().h/4]
        # testing top and bottom collisions
        if object.get_rect().right - collision_offsets[0] > coll_surface.get_rect().left and \
                        object.get_rect().left + collision_offsets[0] < coll_surface.get_rect().right:
            if object.get_rect().top < coll_surface.get_rect().top:
                object.get_rect().bottom = coll_surface.get_rect().top
                y_vel = 0
            if object.get_rect().bottom > coll_surface.get_rect().bottom:
                object.get_rect().top = coll_surface.get_rect().bottom
                y_vel = 0

        # testing left and right collisions
        if object.get_rect().bottom - collision_offsets[1] > coll_surface.get_rect().top and \
                        object.get_rect().top + collision_offsets[1] < coll_surface.get_rect().bottom:
            if object.get_rect().left < coll_surface.get_rect().left:
                object.get_rect().right = coll_surface.get_rect().left
                x_vel = 0
            if object.get_rect().right > coll_surface.get_rect().right:
                object.get_rect().left = coll_surface.get_rect().right
                x_vel = 0

        object.set_vel([x_vel, y_vel])

def is_grounded(object):
    level_objects = objectmanager.get_level_objects()
    level_rects = [levelObject.get_rect() for levelObject in level_objects]
    test_rect = object.get_rect()
    test_rect = test_rect.move(0,1)
    coll_indices = test_rect.collidelistall(level_rects)
    if len(coll_indices) > 0:
        return True
    return False





