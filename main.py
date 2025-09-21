import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # --- groups ---
    updatable = pygame.sprite.Group() # anything with .update(dt)
    drawable = pygame.sprite.Group() # anything with .draw(screen)
    asteroids = pygame.sprite.Group() # all asteroids
    shots = pygame.sprite.Group() 

    # --- containers (set BEFORE creating instances) ---
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    # instances
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()

    
    # --- game loop ---
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # update all
        updatable.update(dt)

        # --- collision check: player vs asteroids ---
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                pygame.quit()
                sys.exit()

        # --- collisions: shots vs asteroids ---
        for asteroid in list(asteroids):
            for shot in list(shots):
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()
                    break

        # draw all
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
