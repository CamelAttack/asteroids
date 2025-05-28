# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import circleshape
from player import Player
from constants import *

# Defining main function
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    center_x = int(SCREEN_WIDTH / 2)
    center_y = int(SCREEN_HEIGHT / 2)
    player_object = Player(center_x, center_y)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player_object.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) /1000
    


# Using the special variable 
# __name__
if __name__=="__main__":
    main()