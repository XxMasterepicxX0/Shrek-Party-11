import pygame
import os

WIDTH, HEIGHT = 900, 500
COLOR = (255,255,255)
FPS = 120
VEL = 2
#C stands for character
C_WIDTH, C_HEIGHT = 55, 40
CHARACTER = pygame.image.load(os.path.join("Assets", "character.png"))
CHARACTER = pygame.transform.scale(CHARACTER, (C_WIDTH, C_HEIGHT))


#Creates window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shrek Party 11")

#players movement
def movement(key_pressed, player):
        #left
        if key_pressed[pygame.K_a]:
             player.x -= VEL
        #right
        if key_pressed[pygame.K_d]:
             player.x += VEL
        #up
        if key_pressed[pygame.K_w]:
             player.y -= VEL
        #down
        if key_pressed[pygame.K_s]:
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

        #I dont know if this work lol
        """
        This should pass the key pressed to the movement function, and the movement function should take that and run it through an if statement.
        However, since the function also uses player, you need to pass player through it. So the function knows who the player is.
        But that's what I believe is going on; I have no idea what I'm doing. 
        """
        key_pressed = pygame.key.get_pressed()
        movement(key_pressed, player)
        
        
        draw_window(player)

    pygame. quit()
        

#Makes it so you only run this function when you run the file
if __name__ == "__main__":
    main()