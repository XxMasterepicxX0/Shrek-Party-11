import pygame, sys
from setting import *
from player import Player


class Game:
    def __init__(self):
        #initialize all imported pygame modules
        pygame.init()
        # Creates window
        self.WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Shrek Party 11")
        #Need for the FPS so it limits the games fps
        self.clock = pygame.time.Clock()

        """
        I will need to come back to this one
        I was planning of having multiple levels but there is a issues with how convert_alpha is proccess
        The goal is to have a background class that will allow for multiple levels
        or I become lazy and say no
        """
        Level1 = pygame.image.load("Assets/background/test_background.jpg").convert_alpha()
        self.back_image = Level1

    # creating the player objects
    player1 = Player(200, 400)
    player2 = Player(700, 400)
    #function used to draw the background
    def draw_background(self):
        self.scaled_ver = pygame.transform.scale(self.back_image, (WIDTH, HEIGHT))
        self.WIN.blit(self.scaled_ver, (0, 0))
    #main game loop
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            #self.WIN.fill(COLOR) <-- not need
                     
            #calls the function responsible for drawing the background
            self.draw_background()
            #uses the objects that were created and draws them using the player class draw function
            self.player1.draw(self.WIN)
            self.player2.draw(self.WIN)
            #uses the movement function to move the players.
            self.player1.movement(WIDTH)
            self.player2.movement(WIDTH)
            #updates the screen
            pygame.display.update()
            #makes the game tick every FPS OR EVERY SET NUMBER
            self.clock.tick(FPS)

#Makes it so you only run this function when you run the file
if __name__ == '__main__':
    game = Game()
    game.run()
