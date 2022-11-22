import pygame
import os

WIDTH, HEIGHT = 900, 500
COLOR = (255, 255, 255)
FPS = 120
VEL = 2

# C stands for character
C_WIDTH, C_HEIGHT = 60, 100
CHARACTER = pygame.image.load(os.path.join("Assets", "character.png"))
CHARACTER = pygame.transform.scale(CHARACTER, (C_WIDTH, C_HEIGHT))
