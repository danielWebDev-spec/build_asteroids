import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # --- groups ---
    updatable = pygame.sprite.Group() # anything with .update(dt)
    drawable = pygame.sprite.Group() # anything with .draw(screen)
    asteroids = pygame.sprite.Group() # all asteroids 

    # --- containers wiring (set BEFORE instantiation) ---
    #  Player should update and draw
    Player.containers = (updatable, drawable)

    # Asteroid should be tracked in all three
    Asteroid.containers = (asteroids, updatable, drawable)

    # AsteroidField only updates (it spawns asteroids; it isn't drawable)
    AsteroidField.containers = (updatable)

    # --- create objects ---
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()

    
    # --- game loop ---
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # updte all
        updatable.update(dt)

        # draw all
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
