import pygame
from core.loop import game_loop
from constants import background_colour
from fireworks.parts import screen
from fireworks.game import game
from setup import Universe
pygame.display.set_caption('Fireworks')
universe = Universe(2)
game_loop(True, background_colour, screen, game, universe)

