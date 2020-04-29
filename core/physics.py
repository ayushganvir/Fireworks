import pygame
import math
import random
from constants import WIDTH, HEIGHT
screen = pygame.display.set_mode()


def generate_angle():
    r = random.uniform(math.pi * 0.5, math.pi * 1.5)
    return r


def distance(x1, y1, x2, y2):
    r2 = ((x2 - x1) ** 2) + ((y2 - y1) ** 2)
    return r2


def gravity(x1, y1, x2, y2, m2):
    vector = Vector(x1, y1, x2, y2)
    r2 = distance(x1, y1, x2, y2)

    if r2 == 0:
        return 10
    g = m2 / r2

    delta_gx = vector.vector_component_x(g)
    delta_gy = vector.vector_component_y(g)
    return delta_gx, delta_gy


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Transform:
    @classmethod
    def x(cls, xval):
        return xval

    @classmethod
    def y(cls, yval):
        return (HEIGHT) - yval

    @classmethod
    def angle(cls, angle):
        return angle


class Vector:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def vector_sum(self):
        length = math.sqrt(
            math.pow(self.x2 - self.x1, 2) +
            math.pow(self.y2 - self.y1, 2))
        return length

    def vector_angle(self):
        angle = Transform.angle(math.atan2((Transform.y(self.y2) - Transform.y(self.y1)), (Transform.x(self.x2) - Transform.x(self.x1))))
        return angle

    def vector_component_x(self, g):
        vector_x = math.cos(self.vector_angle()) * g
        return vector_x

    def vector_component_y(self, g):
        vector_y = math.sin(self.vector_angle()) * g
        return vector_y