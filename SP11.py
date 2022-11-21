import pygame
import os

WIDTH, HEIGHT = 900, 500
COLOR = (255,255,255)
FPS = 120
VEL = 2
#C stands for character
C_WIDTH, C_HEIGHT = 60, 100
CHARACTER = pygame.image.load(os.path.join("Assets", "character.png"))
CHARACTER = pygame.transform.scale(CHARACTER, (C_WIDTH, C_HEIGHT))

#Creates window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shrek Party 11")

#Max_attack = 4
#action_attack = []

#players movement
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

#draws things to the image
def draw_window(player):
    WIN.fill(COLOR)
    WIN.blit(CHARACTER, (player.x,player.y))
    pygame.display.update()

#main game loop
def main():
    player = pygame.Rect(100, 300, C_WIDTH, C_HEIGHT )

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        """        
        if  event.type == pygame.KEYDOWN:
             if event.key == pygame.K_LCTRL and len(action_attack) < Max_attack:
                  attack = pygame.Rect(player.x + player.width, player.y + player.height/2, 5,5 )
                  action_attack.append(attack)
"""  
        #I dont know if this work lol
        """
        This should pass the key pressed to the movement function, and the movement function should take that and run it through an if statement.
        However, since the function also uses player, you need to pass player through it. So the function knows who the player is.
        But that's what I believe is going on; I have no idea what I'm doing.
        """
        key_pressed = pygame.key.get_pressed()
        movement(key_pressed, player)
        
        #print(action_attack)
        draw_window(player)

    pygame. quit()
        

#Makes it so you only run this function when you run the file
if __name__ == "__main__":
    main()