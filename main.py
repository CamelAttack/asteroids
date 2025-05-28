# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

# Defining main function
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
    


# Using the special variable 
# __name__
if __name__=="__main__":
    main()