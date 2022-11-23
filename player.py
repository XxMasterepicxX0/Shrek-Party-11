import pygame

class Player():
    def __init__(self, x, y):
        #creates a rect
        self.rect = pygame.Rect((x, y, 100, 200))

    #draws the player on floor
    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)
