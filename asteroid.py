import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        # draw an outlined circle (width=2)
        pygame.draw.circle(screen, "white", self.position, self.radius,2)

    def update(self, dt):
        # move in a straight line at constant speed
        self.position += self.velocity * dt

    def split(self):
        """
        Kill this asteroid. If it's bigger than the minimum, spawn 2 smaller/faster asteroids that fly apart.
        """
        # remove original
        self.kill()

        # small asteroids don't split further
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # pick a random split angle (degrees) between 20-50
        angle = random.uniform(20, 50)

        # make two new velocity vectors rotated in opposite directions, slightly faster
        v1 = self.velocity.rotate(+angle) * 1.2
        v2 = self.velocity.rotate(-angle) * 1.2

        # child radius is one step smaller
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # spawn two new asteroids at the same position
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = v1

        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a2.velocity = v2 
