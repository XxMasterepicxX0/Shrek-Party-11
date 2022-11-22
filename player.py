import pygame
from setting import *

class Player_CLASS():
    def __init__(self, player, x, y):
        self.player = player
        self.rect = pygame.Rect((x, y, C_WIDTH, C_HEIGHT))

    def movement(key_pressed, player):
        #left
        if key_pressed[pygame.K_a] and player.x - VEL > 0:
             player.x -= VEL
        #right
        if key_pressed[pygame.K_d] and player.x + VEL + player.width < WIDTH:
             player.x += VEL
        #up
        if key_pressed[pygame.K_w] and player.y - VEL > 0 : 
             player.y -= VEL
        #down
        if key_pressed[pygame.K_s] and player.y + VEL + player.height < HEIGHT:
             player.y += VEL