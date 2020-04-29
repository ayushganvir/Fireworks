import math
import random
import pygame
from typing import List

from constants import WIDTH, HEIGHT
screen = pygame.display.set_mode((WIDTH, HEIGHT))


class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Circle has screen color location size in order
class Particle:
    def __init__(self, velocity, angle, color, location, size, mass):
        self.fragment_list = []
        self.is_exploded = False
        self.is_stopped = False
        self.mass = mass
        self.velocity = velocity
        self.angle = angle
        self.color = color
        self.location = location
        self.size = size
        self.velocity_y = self.velocity * math.sin(self.angle)
        self.velocity_x = self.velocity * math.cos(self.angle)

    def display(self):
        pygame.draw.circle(screen, (
            self.color.r, self.color.g, self.color.b),
            (int(self.location.x), int(self.location.y)),
            self.size
        )

    def moving(self, delta_t, gravity):
        if self.is_stopped:
            return
        self.velocity_y -= gravity * delta_t
        self.location.y -= self.velocity_y * delta_t
        self.location.x += self.velocity_x * delta_t

    def exploding(self, no_of_fragments):
        if self.is_exploded:
            return
        self.is_exploded = True
        self.is_stopped = True
        mass_list = [random.randint(1, 20) for i in range(no_of_fragments)]
        total_mass = sum(mass_list)

        for i in range(no_of_fragments):
            fragment_angle = random.uniform(0, 1)
            fragment_mass = self.mass * (mass_list[i] / total_mass)
            momentum = math.hypot(self.velocity_x, self.velocity_y) * self.mass
            fragment_velocity = momentum / fragment_mass
            color = Color(random.randint(0, 200), random.randint(0, 200), random.randint(0, 200))
            self.fragment_list.append(
                Particle(
                    fragment_velocity,
                    math.pi * fragment_angle,
                    color,
                    Point(self.location.x, self.location.y),
                    10, 50
                )
            )