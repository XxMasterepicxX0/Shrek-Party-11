import pygame

class Player():
    def __init__(self, x, y):
        self.rect = pygame.Rect((x, y, 100, 200))

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)
