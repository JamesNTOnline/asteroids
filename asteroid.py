from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):


    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50) # angle between 20 and 50 degrees
            vect_one = self.velocity.rotate(angle)
            vect_two = self.velocity.rotate(-angle) # two vectors in different directions
            new_radius = self.radius - ASTEROID_MIN_RADIUS 
            asteroid_one = Asteroid(self.position.x, self.position.y, new_radius) 
            asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_one.velocity = vect_one * random.uniform(1, 1.5) 
            asteroid_two.velocity = vect_two * random.uniform(1, 1.5)






    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

