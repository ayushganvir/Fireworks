from core.physics import Transform
import time
from constants import height
import random
import constants


def game(universe, game_clock):
    delta_t = game_clock.tick() / 20000.0
    for firework in universe.firework_list:
        if firework.velocity_y > 50:
            firework.moving(delta_t, constants.gravity)
            firework.display()
        else:
            firework.exploding(random.randint(10, 30))
            for frag in firework.fragment_list:
                frag.moving(delta_t, constants.gravity)
                frag.display()
                if Transform.y(frag.location.y) < 10:
                    frag.is_stopped = True
