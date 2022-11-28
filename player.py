import pygame
from setting import *


class Player():
    def __init__(self, x, y):
        # creates a rect
        self.rect = pygame.Rect((x, y, 100, 200))

    # draws the player on floor
    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)

    # Player movement
    def movement(self, WIDTH):
        speed = TEST_C_SPEED
        x = 0
        y = 0

        key_pressed = pygame.key.get_pressed()

        # left
        if key_pressed[pygame.K_a] and self.rect.left + x > 0:
            x -= speed
            print(self.rect.left + x > 0)
        # right
        if key_pressed[pygame.K_d] and self.rect.right + x < WIDTH:
            x += speed
            print(self.rect.right + x < WIDTH)


        self.rect.x += x
        self.rect.y -= y


"""
    Testing
class Player1(Player):
    def __init__(self, x, y):
    x = 500
    y = 180
"""