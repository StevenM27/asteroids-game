from circleshape import *
from constants import *
import random
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)


    def update(self, dt):
        self.position += self.velocity * dt


    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20, 50)

        new_velocity_arr = [self.velocity.rotate(angle), self.velocity.rotate(-angle)]
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        child_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        child_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)

        child_asteroid_1.velocity = new_velocity_arr[0] * 1.2
        child_asteroid_2.velocity = new_velocity_arr[1] * 1.2