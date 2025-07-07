import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    
    def update(self, dt):
        self.position += (self.velocity * dt)

    
    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        rand_split_angle = random.uniform(20, 50)
        left_split = self.velocity.rotate(-rand_split_angle)
        right_split = self.velocity.rotate(rand_split_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        child_ast_left = Asteroid(self.position.x, self.position.y, new_radius)
        child_ast_right = Asteroid(self.position.x, self.position.y, new_radius)
        child_ast_left.velocity = left_split * 1.2
        child_ast_right.velocity = right_split * 1.2

        