import pygame 
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, DRAW_LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius == ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(MINIMUM_RANDOM_RADIUS, MAXIMUM_RANDOM_RADIUS) 
        first_vector = self.velocity.rotate(random_angle)
        second_vector = self.velocity.rotate(-random_angle)
        new_asteroids_radius = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid = Asteroid(self.position.x, self.position.y, new_asteroids_radius)
        new_asteroid.velocity = first_vector * INCREASED_VELOCITY_SCALE
        new_asteroid = Asteroid(self.position.x, self.position.y, new_asteroids_radius)
        new_asteroid.velocity = second_vector * INCREASED_VELOCITY_SCALE
