from fireworks.parts import Point, Particle, Color
import math
import random
from core.physics import Transform
from constants import WIDTH, HEIGHT


class Universe:
    def __init__(self, no_of_fireworks):
        self.firework_list = []
        for i in range(no_of_fireworks):
            self.firework_list.append(
                Particle(
                    random.uniform(7000, 10000),
                    math.pi * random.uniform(0.45, 0.55),
                    Color(255, 255, 255),
                    Point(Transform.x(random.randint(0, WIDTH)), Transform.y(0)),
                    20, random.uniform(10, 100)
                )
            )
