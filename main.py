import pygame, sys
from setting import *
from player import Player


class Game:
    def __init__(self):

        pygame.init()

        self.WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Shrek Party 11")

        self.clock = pygame.time.Clock()

        Level1 = pygame.image.load("Assets/background/test_background.jpg").convert_alpha()

        self.back_image = Level1

    player1 = Player(200, 400)
    player2 = Player(700, 400)

    def draw_background(self):
        self.scaled_ver = pygame.transform.scale(self.back_image, (WIDTH, HEIGHT))
        self.WIN.blit(self.scaled_ver, (0, 0))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.WIN.fill(COLOR)
            self.draw_background()
            self.player1.draw(self.WIN)
            self.player2.draw(self.WIN)
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
