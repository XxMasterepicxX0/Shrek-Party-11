import pygame
import os
from main import *

class BackGround:
    def __init__(self):
        self.bg_image = pygame.image.load(os.path.join("main_menu", "test_bacground.jpg")).convert_alpha()

    def draw_background(self):
        self.WIN.blit(self.bg_image, (0,0))
    
