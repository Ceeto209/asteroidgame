import sys
import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    Clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    dt = 0

    while pygame.get_init() == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, "black")
        for item in updatable:
            item.update(dt)

        for asteroid in asteroids:
            if asteroid.collisions(player):
                print("Game Over")
                sys.exit()
                print("Game Over")
                pygame.QUIT
            for shot in shots:
                if asteroid.collisions(shot):
                    shot.kill()
                    asteroid.split()

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()
        timePassed = Clock.tick(60)
        dt = timePassed / 1000
        
if __name__ == "__main__":
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    main()
    
