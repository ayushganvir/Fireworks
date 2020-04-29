import pygame


def game_loop(running, background_colour, screen, game, universe):
    game_clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(background_colour)
        game(universe, game_clock)
        pygame.display.update()

