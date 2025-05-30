# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
import circleshape
from asteroid import Asteroid
from player import Player
from asteroidfield import AsteroidField
from constants import *

# Defining main function
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    

    center_x = int(SCREEN_WIDTH / 2)
    center_y = int(SCREEN_HEIGHT / 2)
    player_object = Player(center_x, center_y)
    asteroid_field = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for some_object in drawable:
            some_object.draw(screen)
        for some_asteroid in asteroids:
            if some_asteroid.collides_with(player_object):
                print("Game over!")
                sys.exit()
        pygame.display.flip()
        dt = clock.tick(60) /1000
    


# Using the special variable 
# __name__
if __name__=="__main__":
    main()