import pygame
import sys
from pygame.locals import QUIT

from constants import FPS, HEIGHT, WIDTH, GAME_NAME, CHARACTER_IMG
import colors as c
from game_objects.character import Player

pygame.init()

FPS_RATE = pygame.time.Clock()

# Create display
game_window = pygame.display.set_mode((WIDTH, HEIGHT))
game_window.fill(c.WHITE)
pygame.display.set_caption(GAME_NAME)
pygame.display.init()


def main_game():
    running = True
    player = Player(
                    CHARACTER_IMG,
                    16,
                    16,
                    WIDTH // 2,
                    HEIGHT // 2,
                    1)
    while running:
        # Quit game
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        # initialize player
        player.update()
        game_window.fill(c.GREY)
        player.draw(game_window)
        pygame.display.flip()
        FPS_RATE.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main_game()
