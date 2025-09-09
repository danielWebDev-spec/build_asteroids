import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        # draw an outlined circle (width=2)
        pygame.draw.circle(screen, "white", self.position, self.radius,2)

    def update(self, dt):
        # move in a straight line at constant speed
        self.position += self.velocity * dt